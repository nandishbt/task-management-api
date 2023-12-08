from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(title='Test Task', description='Test Description', due_date='2023-12-31', status='Pending')

    def test_get_task_list(self):
        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more test cases for other CRUD operations
