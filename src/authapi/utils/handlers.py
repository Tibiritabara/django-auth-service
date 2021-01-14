"""
This are a collection of methods for exception handling making
the endpoint responses standarized and more manageable in case
we use custom exceptions
"""
import json
from django.http import HttpResponseNotFound
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    else:
        if isinstance(exc, TypeError):
            response = Response(
                {
                    "detail": "attribute %s" % exc.__str__(),
                    "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY
                },
                status=status.HTTP_422_UNPROCESSABLE_ENTITY
            )
        else:
            response = Response(
                {
                    "detail": "%s" % exc.__str__(),
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return response


def view_404_exception(request, exception):
    response_data = {
        "detail": 'The requested endpoint does not exist. Please communicate with the API administrator.',
        "status_code": status.HTTP_404_NOT_FOUND
    }
    return HttpResponseNotFound(json.dumps(response_data), content_type="application/json")
