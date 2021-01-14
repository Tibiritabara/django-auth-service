"""
Tests related with user operations
"""
import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt import utils

from authapi.models import User


# Create your tests here.
class JWTAuthenticationTest(TestCase):
    """JWT Authentication Tests"""

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.email = 'pepito.perez@example.com'
        self.user = User.objects.create_superuser(self.email, password="Test123")

    def test_login(self):
        """
        Ensure POSTing form over JWT auth with correct credentials
        passes and does not require CSRF
        """

        # payload = utils.jwt_payload_handler(self.user)
        # token = utils.jwt_encode_handler(payload)
        #
        # auth = 'Bearer {0}'.format(token)
        response = self.csrf_client.post(
            '/auth/login',
            {'email': 'pepito.perez@example.com', 'password': 'Test123'},
            # HTTP_AUTHORIZATION=auth
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        payload = json.loads(response.content)
        self.assertIsInstance(payload, dict)
        self.assertEqual(set(payload.keys()), {'token'})

    def test_verify(self):
        """
        Ensure POSTing form over JWT auth with correct credentials
        passes and does not require CSRF
        """

        # payload = utils.jwt_payload_handler(self.user)
        # token = utils.jwt_encode_handler(payload)
        #
        # auth = 'Bearer {0}'.format(token)
        response = self.csrf_client.post(
            '/auth/login',
            {'email': 'pepito.perez@example.com', 'password': 'Test123'},
            # HTTP_AUTHORIZATION=auth
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh(self):
        """
        Ensure POSTing form over JWT auth with correct credentials
        passes and does not require CSRF
        """

        # payload = utils.jwt_payload_handler(self.user)
        # token = utils.jwt_encode_handler(payload)
        #
        # auth = 'Bearer {0}'.format(token)
        response = self.csrf_client.post(
            '/auth/login',
            {'email': 'pepito.perez@example.com', 'password': 'Test123'},
            # HTTP_AUTHORIZATION=auth
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_details(self):
        """
        Ensure POSTing form over JWT auth with correct credentials
        passes and does not require CSRF
        """

        # payload = utils.jwt_payload_handler(self.user)
        # token = utils.jwt_encode_handler(payload)
        #
        # auth = 'Bearer {0}'.format(token)
        response = self.csrf_client.post(
            '/auth/login',
            {'email': 'pepito.perez@example.com', 'password': 'Test123'},
            # HTTP_AUTHORIZATION=auth
        )

        payload = json.loads(response.content)

        auth = 'Bearer {0}'.format(payload.get('token'))
        response_details = self.csrf_client.get(
            '/auth/user',
            HTTP_AUTHORIZATION=auth,
        )
        details_payload = json.loads(response_details.content)
        self.assertEqual(response_details.status_code, status.HTTP_200_OK)
        self.assertIsInstance(details_payload, dict)
        self.assertEqual(
            set(details_payload.keys()),
            {
                'id',
                'last_login',
                'is_superuser',
                'first_name',
                'last_name',
                'is_staff',
                'is_active',
                'date_joined',
                'email',
                'groups',
                'user_permissions',
                'phone_number',
            }
        )
