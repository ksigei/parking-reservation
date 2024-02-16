from django.test import TestCase
from user_auth.models import CustomUser
from user_auth.forms import CustomAuthenticationForm
from django.contrib.auth import authenticate

class CustomUserModelTestCase(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(email='test@example.com', password='password123')
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertIsNotNone(user.password)

    def test_create_superuser(self):
        admin_user = CustomUser.objects.create_superuser(email='admin@testt.com', password='1234')
        self.assertEqual(admin_user.email, 'admin@testt.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_active)

class CustomAuthenticationFormTestCase(TestCase):
    def test_invalid_authentication(self):
        # auth using invalid credentials
        form = CustomAuthenticationForm(data={'email': 'invalidmail@testttt.com', 'password': 'invalid_pw'})
        self.assertFalse(form.is_valid())
        error = form.errors['__all__'][0]
        self.assertEqual(error, 'Invalid email, username, or password')

    def test_authentication_no_data(self):
        # auth with no data
        form = CustomAuthenticationForm(data={})
        self.assertFalse(form.is_valid())
