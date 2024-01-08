from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
import uuid


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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.email
