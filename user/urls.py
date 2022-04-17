from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register(r"signup", views.SignUpUserView)
router.register(r"update_user", views.UserProfileUpdateView)
router.register(r"profiles", views.UserViewSet)

urlpatterns = [
    path("users/", include(router.urls)),
]
