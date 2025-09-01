from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='tasker@example.com', username='tasker', password='pass12345')
        token = self.client.post(reverse('token-obtain'), {"email":"tasker@example.com", "password":"pass12345"}, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_create_task(self):
        url = reverse('tasks-list-create')
        data = {"title": "My Task", "description": "Do something"}
        r = self.client.post(url, data, format='json')
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data['title'], "My Task")

    def test_owner_only_delete(self):
        # create by user
        create = self.client.post(reverse('tasks-list-create'), {"title": "T1"}, format='json')
        pk = create.data['id']
        # try delete as another user
        other = User.objects.create_user(email='other@example.com', username='other', password='pass2222')
        token2 = self.client.post(reverse('token-obtain'), {"email":"other@example.com", "password":"pass2222"}, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token2}')
        r = self.client.delete(reverse('task-detail', kwargs={'pk': pk}))
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
