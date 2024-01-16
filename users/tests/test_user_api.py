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

    def test_create_user_endpoint_success(self):
        """Test user creation API endpoint"""
        payload = {
            'username': 'johndoe',
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        res = self.client.post('/auth/users/', data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_get_user_tokens(self):
        """Test getting user access and refresh token"""
        payload = {
            'username': 'johndoe',
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        self.client.post('/auth/users/', data=payload)
        res = self.client.post('/auth/jwt/create', data=payload)
        # print(res.data)
        self.assertIn('refresh', res.data)
        self.assertIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_user_access_token_refresh(self):
        """Test getting user access being refreshed"""
        payload = {
            'username': 'johndoe',
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        self.client.post('/auth/users/', data=payload)
        res = self.client.post('/auth/jwt/create', data=payload)
        payload2 = {
            'refresh': res.data['refresh']
        }
        self.client.post('/auth/jwt/refresh', data=payload2)
        # print(res.data)
        self.assertIn('access', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class PrivateUserApiTests(TestCase):
    """Test authenticated user API endpoints"""

    def setUp(self) -> None:
        self.client = APIClient()

        payload = {
            'username': 'johndoe',
            'email': 'test@example.com',
            'password': 'testpass123',
        }
        self.user = create_user()
        self.client.force_authenticate(user=self.user)

    def retrieve_user_success(self):
        """Test retrieve user details successfully"""
        res = self.client.get('/auth/users/me', follow=True, format='json')

        self.assertEqual(res.data['email'], self.user.email)
        self.assertEqual(res.data['username'], self.user.username)
        self.assertEqual(res.data['role'], self.user.role)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEquals(get_user_model().objects.count(), 1)

    def test_user_delete(self):
        """Testing user delete"""
        res = self.client.delete('/auth/users/me', follow=True, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
