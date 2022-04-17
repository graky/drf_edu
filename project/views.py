from rest_framework import viewsets, mixins
from rest_framework import permissions, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from project.types import ProjectSerializer, StageSerializer
from project.models import Project, Stage


class ProjectView(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.ListAPIView,
    viewsets.GenericViewSet,
):
    queryset = Project.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProjectSerializer


class StageView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Stage.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = StageSerializer
