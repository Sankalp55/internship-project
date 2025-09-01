from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_register(self):
        url = reverse('register')
        data = {
            "email": "tester@example.com",
            "username": "tester",
            "name": "Test User",
            "password": "StrongPassw0rd!",
            "password2": "StrongPassw0rd!"
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email='tester@example.com').exists())

    def test_token_and_profile(self):
        user = User.objects.create_user(email='foo@x.com', username='foo', password='pass12345')
        token_url = reverse('token-obtain')
        resp = self.client.post(token_url, {"email":"foo@x.com", "password":"pass12345"}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        access = resp.data.get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access}')
        profile_url = reverse('profile')
        p = self.client.get(profile_url)
        self.assertEqual(p.status_code, status.HTTP_200_OK)
        self.assertEqual(p.data['email'], 'foo@x.com')
