"""
GraphQL inputs and objects for mutations
"""
import graphene
import graphql_jwt
from graphene import InputObjectType
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation

from authapi.exceptions import NotAuthenticatedException
from authapi.models import User
from authapi.queries import UserType


class CreateUserInput(InputObjectType):
    """
    Fields requested for new user creation
    """
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    password = graphene.String(required=True)
    phone = graphene.String(required=True)


class UpdateUserInput(InputObjectType):
    """
    Available fields for the update operation.
    """
    email = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    password = graphene.String()
    phone = graphene.String()


class CreateUserMutation(graphene.Mutation):
    """
    Mutation to create a new user with Graphene.
    """
    class Arguments:
        input  = CreateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, input=None):
        user = User()
        user.set_password(input.pop('password'))
        for key, value in input.items():
            setattr(user, key, value)
        user.save()

        return CreateUserMutation(user=user)


class UpdateUserMutation(graphene.Mutation):
    """
    Mutation to update existing users. Any value can be updated independently
    """
    class Arguments:
        input = UpdateUserInput(required=True)

    user = graphene.Field(UserType)

    def mutate(self, info, input=None):
        user = info.context.user
        if user.is_anonymous:
            raise NotAuthenticatedException()
        for key, value in input.items():
            if key == "password":
                user.set_password(value)
                continue
            setattr(user, key, value)
        user.save()
        return UpdateUserMutation(user=user)


class Mutation(graphene.ObjectType):
    """
    Naming and definition of mutations
    """
    create_user = CreateUserMutation.Field()
    update_user = UpdateUserMutation.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
