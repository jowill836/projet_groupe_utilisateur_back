from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UsrsTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/Usrs/'
    def test_Usrs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.

class ConfigurationTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/Configuration/'
    def test_Usrs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GrpTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/Grp/'
    def test_Usrs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

