from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


@api_view(['GET'])
@permission_classes((AllowAny, ))
def api_root(request):
    return JsonResponse({"Hello":"World"}, status=status.HTTP_200_OK)


class UserView(generics.RetrieveAPIView):
    """
    This class replaces the basic userView from django to return
    the user data based on the JWT token sent on the request.
    """

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {self.lookup_field: self.request.user.id, 'is_active': True}
        obj = generics.get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj
