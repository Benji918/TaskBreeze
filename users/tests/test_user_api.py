from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


def create_user(**params):
    """Create and return user"""
    defaults = {
        'email': 'johndoe@example.com',
        'password': 'testpass123',
        'username': 'johndoe',
    }

    defaults.update(params)
    user = get_user_model().objects.create_user(**defaults)
    return user


class PublicUserApiTests(TestCase):
    """Testing public(unauthenticated) features of API"""

    def setUp(self) -> None:
        self.client = APIClient()
