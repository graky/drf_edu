from rest_framework import routers
from user import views


main_router = routers.DefaultRouter()
main_router.register(r'users', views.UserViewSet)
main_router.register(r'groups', views.GroupViewSet)