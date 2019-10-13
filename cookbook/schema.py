import graphene

import cookbook.ingredients.schema

class Query(cookbook.ingredients.schema.Query, graphene.ObjectType):
    pass
schema=graphene.Schema(query=Query)