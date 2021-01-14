"""
Custom user routes and endpoints
"""
from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

from .views import UserView  # we must implement this

urlpatterns = [
    # endpoints from Django REST framework JWT package
    path('login', obtain_jwt_token, name='login'),
    path('verify', verify_jwt_token, name='verify'),
    path('refresh', refresh_jwt_token, name='refresh'),
    path('user', UserView.as_view(), name='user')
]
