""" 
This module will override the way django creates users and the way it handles 
usernames and emails.
"""
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """ 
    This class inherits from django user manager and it allow us to 
    customize the way we expect the framework to create the users.
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        This method must return user.
        :argument str email: valid email 
        :argument str password:  Contrasenia valida del usuario
        """

        # if email is None, throw error
        if not email:
            raise ValueError('This field cannot be null.')

        # fixing email formatting (e.g. transferring to lowercase)
        email = self.normalize_email(email)

        # creating user model
        user = self.model(email=email, **extra_fields)

        # setting password for our new user
        user.set_password(password)

        # saving to database
        user.save(using=self._db)

        # returning user
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Wrapper method for creating normal user.
        This method must return user.
        """

        # method input validation
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        # returning user
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Wrapper method for creating admin user.
        This method must return user.
        """

        # method input validation
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # returning user
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ 
    Customization of django base class for user storage.
    """
    # don't use username
    username = None

    email = models.EmailField(
        'Email address of the user.', 
        unique=True,
    )

    phone_number = models.CharField(
        'Phone number of the user', 
        null=True, 
        max_length=15,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()
