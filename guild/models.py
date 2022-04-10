from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Guild(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name="Guild name")
    description = models.TextField(verbose_name="Guild description")
    creator = models.ForeignKey(to=User, verbose_name="Guild creator",
        on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Member(models.Model):
    class PositionEnum(models.TextChoices):
        ADMIN = "ADMIN"
        MODERATOR = "MODERATOR"
    user = models.ForeignKey(to=User, verbose_name="Guild", on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    position = models.CharField(max_length=21,
                                choices=PositionEnum.choices,
                                null=True,
                                blank=True,
                                default="",
                                verbose_name="User position",
                                )

    class Meta:
        abstract = True


class GuildMember(Member, models.Model):
    guild = models.ForeignKey(to=Guild, verbose_name="Guild", on_delete=models.CASCADE)


class GuildTeam(models.Model):
    name = models.CharField(max_length=100, verbose_name="Team in guild")
    description = models.TextField(verbose_name="Team description")
    leader = models.ForeignKey(to=User, on_delete=models.CASCADE)


class TeamMember(Member, models.Model):
    team = models.ForeignKey(to=GuildTeam, on_delete=models.CASCADE)
