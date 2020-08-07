import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import db_session, UserAddress as UserAddressModel, Users as UserModel, Posts as PostModel, Comments as CommentModel


class UserAddress(SQLAlchemyObjectType):
    class Meta:
        model = UserAddressModel
        interfaces = (relay.Node, )


class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class Posts(SQLAlchemyObjectType):
    class Meta:
        model = PostModel
        interfaces = (relay.Node, )


class Comments(SQLAlchemyObjectType):
    class Meta:
        model = CommentModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_user_addresses = SQLAlchemyConnectionField(Users.connection)
    all_users = SQLAlchemyConnectionField(
        Users.connection, sort=None)
    all_posts = SQLAlchemyConnectionField(
        Posts.connection, sort=None)
    all_comments = SQLAlchemyConnectionField(
        Comments.connection, sort=None)


schema = graphene.Schema(query=Query)
