"""
GraphQL Queries and objects
"""
import graphene
from graphene import ObjectType, relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from authapi.exceptions import NotAuthenticatedException
from authapi.models import User


class UserType(DjangoObjectType):
    """
    User type definition for Graphene
    """
    class Meta:
        model = User
        exclude = (
            'password',
        )


class Query(graphene.ObjectType):
    """
    Graphene queries definitions
    """
    me = graphene.Field(UserType)

    def resolve_me(
        self,
        info,
        **kwargs,
    ):
        user = info.context.user
        if user.is_anonymous:
            raise NotAuthenticatedException()
        return user
