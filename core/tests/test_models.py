from django.test import TestCase
from core import models
from django.contrib.auth import get_user_model


def create_user(**params):
    """Create and return user"""
    defaults = {
        'email': 'johndoe@example.com',
        'password': 'testpass123',
        'username': 'johndoe',
    }

    defaults.update(**params)
    user = get_user_model().objects.create_user(**params)
    return user


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_success(self):
        """Test user creation successfully"""
        email = 'kodi@example.com'
        password = 'testpass12345'
        user = create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))