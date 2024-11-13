from django.test import TestCase
from django.urls import reverse
from intro_proj.models import User

class LoginTests(TestCase):
    def setUp(self):
        self.test_data = {'username':'John User', 'email':'user@sandiego.edu', 'password': 'passw0rd'}

    def tearDown(self):
        pass

    def test_register(self):
        self.client.post(reverse('register'), self.test_data)
        self.assertTrue(User.objects.filter(email='user@sandiego.edu').exists())
    
    def test_duplicate_emails(self):
        self.client.post(reverse('register'), self.test_data)
        self.client.post(reverse('register'), {'username':'a', 'email':'user@sandiego.edu', 'password':'pass'})
        self.assertEqual(User.objects.filter(email='user@sandiego.edu').count(), 1)

    def test_login_success(self):
        self.client.post(reverse('register'), self.test_data)
        response = self.client.post(reverse('login'), {'username':'John User', 'password': 'passw0rd'})
        self.assertEqual(response.status_code, 302)
    
    def test_bad_pass(self):
        self.client.post(reverse('register'), self.test_data)
        response = self.client.post(reverse('login'), {'username':'John User', 'password': 'notmypass'})
        self.assertEqual(response.status_code, 200)
    
    def test_bad_user(self):
        self.client.post(reverse('register'), self.test_data)
        response = self.client.post(reverse('login'), {'username':'Jane User', 'password': 'passw0rd'})
        self.assertEqual(response.status_code, 200)
    
    def test_bad_both(self):
        self.client.post(reverse('register'), self.test_data)
        response = self.client.post(reverse('login'), {'username':'Jane User', 'password': 'notmypass'})
        self.assertEqual(response.status_code, 200)
    
    def test_blank_name(self):
        self.client.post(reverse('register'), {'username':'', 'email':'user@sandiego.edu', 'password': 'passw0rd'})
        self.assertFalse(User.objects.filter(email='user@sandiego.edu').exists())
    
    def test_blank_email(self):
        self.client.post(reverse('register'), {'username':'John User', 'email':'', 'password': 'passw0rd'})
        self.assertFalse(User.objects.filter(username='John User').exists())
    
    def test_blank_pass(self):
        self.client.post(reverse('register'), {'username':'John User', 'email':'user@sandiego.edu', 'password': ''})
        self.assertFalse(User.objects.filter(email='user@sandiego.edu').exists())
        
    def test_logout(self):
        # Log in the user
        self.client.login(username='John User', password='passw0rd')
        
        # Ensure the user is logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

        # Log out the user
        response = self.client.get(reverse('logout'))
        
        # Check the response
        self.assertEqual(response.status_code, 302)  # Assuming logout redirects to another page
        
        # Follow the redirect
        response = self.client.get(response.url)
        
        # Ensure the user is logged out
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login page
        self.assertFalse(response.context['user'].is_authenticated)