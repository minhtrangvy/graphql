from graphene import ObjectType, String

from app.modules.users.queries import UserQuery
from app.modules.users.mutations import UserMutation

class ExampleQuery(ObjectType):
    hello = String()
    
    def resolve_hello(self, info):
        return "Hello"

class RootQuery(ExampleQuery, ObjectType):
    pass

# class RootQuery(UserQuery, ObjectType):
#     pass

# class RootMutation(UserMutation, ObjectType):
#     pass

schema = Schema(query=RootQuery)