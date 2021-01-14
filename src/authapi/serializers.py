"""
This module will contain the serializers for our user class
"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

# getting our current User model
# It's good practice to use get_user_model() method
User = get_user_model()

# Classic model serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # we don't want to return password
        exclude = ['password',]
