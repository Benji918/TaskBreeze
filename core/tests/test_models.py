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

    defaults.update(params)
    user = get_user_model().objects.create_user(**defaults)
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

    def test_create_user_with_blank_email(self):
        """Test creating user with blank email """
        with self.assertRaises(ValueError):
            create_user(email='', password='testpass')

    def test_create_user_with_admin_false(self):
        """Test creating user with is_admin false"""
        user = create_user()

        self.assertFalse(user.is_admin)

    def test_create_superuser(self):
        """Test creation of superuser"""
        email = 'test@example.com'
        password = '123456789'
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_task_creation(self):
        """Test creation of tasks"""
        user = create_user()
        task = models.Task.objects.create(
            title='New_task',
            description='task_description',
            user=user,
        )

        self.assertEqual(task.status, 'open')
        self.assertEqual(task.priority, 'low')
        self.assertEqual(task.user, user)

    def test_task_comment_creation(self):
        """Test task comment creation"""
        user = create_user()
        task = models.Task.objects.create(
            title='New_task',
            description='task_description',
            user=user,
        )
        task_comment = models.TaskComment.objects.create(
            task=task,
            user=user,
            comment='This is a task comment'
        )

        self.assertEquals(task_comment.task, task)
        self.assertEquals(task_comment.user, user)
