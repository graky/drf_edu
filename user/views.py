from rest_framework import viewsets, mixins
from rest_framework import permissions, generics, authentication
from user.types import ProfileSerializer, SignupSerializer, ProfileUpdateSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(generics.ListAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class SignUpUserView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = get_user_model().objects.all()
    serializer_class = SignupSerializer


class UserProfileUpdateView(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProfileUpdateSerializer
