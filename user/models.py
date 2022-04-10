from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(blank=False, unique=True, max_length=30)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_birthday = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    avatar = models.FileField(upload_to="avatars", null=True, blank=True)
    sex = models.CharField(max_length=1, null=True, blank=True)
    skills = ArrayField(models.TextField(), default=list)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username

    def get_skills(self):
        return self.skills

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "auth_user"
