from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import uuid
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('admin', 'admin'),
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    username = models.CharField(_('first_name'), unique=True, max_length=50, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email


class Task(models.Model):
    STATUS_CHOICES = (
        ('open', 'open'),
        ('in progress', 'in progress'),
        ('completed', 'completed'),
    )
    PRIORITY_CHOICES = (
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    title = models.CharField(unique=True, max_length=50, blank=False, null=False)
    description = models.CharField(unique=True, max_length=50, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    due_date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
