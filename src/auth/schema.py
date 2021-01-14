"""
Graphene schema definition
"""
import authapi.mutations
import authapi.queries
import graphene


class Query(
    authapi.queries.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    authapi.mutations.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
