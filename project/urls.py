from django.urls import path, include
from rest_framework.routers import DefaultRouter
from project import views

router = DefaultRouter()
router.register(r"projects", views.ProjectView)
router.register(r"stage", views.StageView)

urlpatterns = [
    path("projects/", include(router.urls)),
]
