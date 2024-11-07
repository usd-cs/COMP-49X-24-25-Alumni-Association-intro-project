from django.test import TestCase
from intro_proj.models import User

# Create your tests here.

class DatabaseTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation(self):
        test_user = User.objects.create(email='user@sandiego.edu', name='John User')
        user = User.objects.get(email='user@sandiego.edu')
        self.assertEqual('user@sandiego.edu', user.email)
    