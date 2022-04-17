from rest_framework import viewsets, mixins
from rest_framework import permissions, generics, authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from guild.types import (
    GuildSerializer,
    GuildMemberSerializer,
    TeamSerializer,
    TeamMemberSerializer,
)
from guild.models import Guild, GuildMember, GuildTeam, TeamMember
from django.contrib.auth import get_user_model

User = get_user_model()


class GuildView(mixins.CreateModelMixin, generics.ListAPIView, viewsets.GenericViewSet):
    queryset = Guild.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GuildSerializer


class GuildMemberView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = GuildMember.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GuildMemberSerializer


class GuildTeamView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = GuildTeam.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TeamSerializer


class TeamMemberView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = TeamMember.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TeamMemberSerializer
