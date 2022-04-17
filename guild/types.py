from rest_framework import serializers
from django.contrib.auth import get_user_model
from guild.models import Guild, GuildTeam, GuildMember, TeamMember
from user.types import ProfileSerializer
from django.db.models import Q

User = get_user_model()


class MemberSerializer(serializers.Serializer):
    class Meta:
        fields = ["user", "role", "position"]

    role = serializers.CharField()
    position = serializers.CharField()
    user = ProfileSerializer()


class GuildMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuildMember
        fields = "__all__"

    def validate_guild(self, value):
        user = self.context["request"].user
        if (
            value.creator != user
            and not GuildMember.objects.filter(
                Q(guild=value) & Q(user=user) & Q(position="ADMIN")
            ).exists()
        ):
            raise serializers.ValidationError(
                {"guild": "You are not guild creator or guild admin"}
            )
        return value

    def create(self, validated_data):
        member = GuildMember(**validated_data)
        member.save()
        return member


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"

    def validate_team(self, value):
        user = self.context["request"].user
        if (
            value.leader != user
            and not TeamMember.objects.filter(
                Q(team=value)
                & Q(user=user)
                & (Q(position="MODERATOR") | Q(position="ADMIN"))
            ).exists()
        ):
            raise serializers.ValidationError(
                {"team": "You are not team leder or not Moderator"}
            )
        return value

    def create(self, validated_data):
        member = TeamMember(**validated_data)
        member.save()
        return member


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuildTeam
        fields = ["name", "description", "leader", "team_members", "guild"]

    team_members = MemberSerializer(
        many=True,
        read_only=True,
    )

    def validate_guild(self, value):
        user = self.context["request"].user
        if not (
            GuildMember.objects.filter(user=user, guild=value).exists()
            or value.creator == user
        ):
            raise serializers.ValidationError({"guild": "You are not guild member"})
        return value

    def create(self, validated_data):
        team = GuildTeam(**validated_data)
        team.save()
        return team


class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = ["title", "description", "creator", "guild_members", "teams"]

    teams = TeamSerializer(many=True, read_only=True)
    guild_members = MemberSerializer(
        many=True,
        read_only=True,
    )

    creator = ProfileSerializer(read_only=True)

    def create(self, validated_data):
        guild = Guild(**validated_data)
        user = self.context["request"].user
        guild.creator = user
        guild.save()
        return guild
