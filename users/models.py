from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """Менеджер для создания пользователя по email."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email обязателен для заполнения')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('Email', unique=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        