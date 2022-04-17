from rest_framework import serializers
from django.contrib.auth import get_user_model
from guild.models import Guild, GuildTeam, GuildMember, TeamMember
from project.models import Project, Stage
from user.types import ProfileSerializer
from itertools import chain

User = get_user_model()


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"

    author = ProfileSerializer(read_only=True)

    def validate_project(self, value):
        user = self.context["request"].user
        user_guilds = list(
            chain(
                Guild.objects.filter(creator=user),
                GuildMember.objects.filter(user=user).values_list("guild", flat=True),
                GuildTeam.objects.filter(leader=user).values_list("guild", flat=True),
                TeamMember.objects.filter(user=user).values_list(
                    "team__guild", flat=True
                ),
            )
        )
        if value.guild.pk not in user_guilds:
            raise serializers.ValidationError({"project": "You are not guild member"})
        return value

    def create(self, validated_data):
        user = self.context["request"].user
        stage = Stage(**validated_data)
        stage.author = user
        stage.save()
        return stage


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "status",
            "creator",
            "guild",
            "created",
            "stages",
        ]
    status = serializers.CharField(required=False)
    stages = StageSerializer(many=True, read_only=True)
    creator = ProfileSerializer(read_only=True)

    def create(self, validated_data):
        if validated_data.get("status"):
            del validated_data["status"]
        project = Project(**validated_data)
        user = self.context["request"].user
        project.creator = user
        project.status = "NOT_TAKEN"
        project.save()
        return project

    def update(self, instance, validated_data):
        user = self.context["request"].user
        if user != instance.creator:
            raise serializers.ValidationError(
                {"authorize": "You dont have permission for this project"}
            )
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
