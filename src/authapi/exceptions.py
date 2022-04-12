
"""
Set of custom exceptions
"""
from rest_framework.exceptions import APIException


class NotAuthenticatedException(APIException):
    """
    Custom exception for unauthorized users
    """
    status_code = 401
    default_detail = 'User is not authorized to execute this action.'
    default_code = 'NOT_AUTHORIZED '


class UnexpectedException(APIException):
    status_code = 500
    defalt_detail = 'Unexpected error occurred.'
    default_code = 'UNEXPECTED_ERROR'
