from django.db import models
from django.contrib.auth import get_user_model
from guild.models import Guild

User = get_user_model()


class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        NOT_TAKEN = "NOT_TAKEN"
        STARTED = "STARTED"
        BEGINNING = "BEGINNING"
        MIDDLE = "MIDDLE"

    title = models.CharField(max_length=100, verbose_name="Project name")
    description = models.TextField(verbose_name="Project description")
    status = models.CharField(max_length=21, choices=ProjectStatus.choices, default="NOT_TAKEN")
    creator = models.ForeignKey(
        to=User, verbose_name="Project creator", on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        to=Guild,
        null=True,
        blank=True,
        related_name="projects",
        on_delete=models.DO_NOTHING,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]


class Stage(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(
        to=Project, related_name="stages", on_delete=models.CASCADE
    )
    content = models.TextField()
    link = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]
