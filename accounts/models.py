from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, username, role, password=None):
        if not username:
            raise ValueError("The Username field must be set")

        user = self.model(username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, role, password=None):
        user = self.create_user(username, role, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    MAKERS = 1
    CHECKERS = 2

    ROLE_CHOICES = (
        (MAKERS, "Makers"),
        (CHECKERS, "Checkers"),
    )

    username = models.CharField(max_length=30, unique=True)
    role = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, default=MAKERS, null=True, blank=True
    )
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["role"]

    def __str__(self):
        return self.username
