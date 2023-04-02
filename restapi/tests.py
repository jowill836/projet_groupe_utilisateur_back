from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UsrsTestCase(APITestCase):
    def setUp(self):
        self.url = 'http://localhost:8000/Usrs/'
    def test_Usrs(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    def test_usrs_create(self):
        data = {'nameusr': 'utilisateurdetest'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


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
    def test_grp_create(self):
        data = {'namegrp': 'grptest'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
