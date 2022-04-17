from django.urls import path, include
from rest_framework.routers import DefaultRouter
from guild import views

router = DefaultRouter()
router.register(r"guild", views.GuildView)
router.register(r"guild_member", views.GuildMemberView)
router.register(r"guild_team", views.GuildTeamView)
router.register(r"team_member", views.TeamMemberView)

urlpatterns = [
    path("guilds/", include(router.urls)),
]
