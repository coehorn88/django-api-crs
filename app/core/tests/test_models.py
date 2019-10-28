from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with email is successful"""
        email = "dummy@email.com"
        password = "hardpassw123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_addres_is_normalized(self):
        """Test the email for a new user is normalized."""
        email = "dummy@EMAILDOMAIN.cOM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_email_is_invalid(self):
        """Test creating user with no email address raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser("dummy@gumail.com", 'test123')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
