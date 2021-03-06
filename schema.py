import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import db_session, UserAddress as UserAddressModel, Users as UserModel, Posts as PostModel, Comments as CommentModel
from .mutations import UpdatePost, DeletePost
from .query_types import UserAddress, Users, Posts, Comments





class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_user_addresses = SQLAlchemyConnectionField(UserAddress.connection)
    all_users = SQLAlchemyConnectionField(
        Users.connection, sort=None)
    all_posts = SQLAlchemyConnectionField(
        Posts.connection, sort=None)
    all_comments = SQLAlchemyConnectionField(
        Comments.connection, sort=None)
    user_by_id = graphene.Field(Users, user_id=graphene.Int(required=True, default_value=None))
    post_by_id = graphene.Field(Posts, post_id=graphene.String(required=True, default_value=None))
    comment_by_id = graphene.Field(Comments, comment_id=graphene.String(required=True, default_value=None))

    def resolve_user_by_id(self, info, user_id=None):
        print(user_id)
        return db_session.query(UserModel).filter_by(id=user_id).first()


    def resolve_post_by_id(self, info, post_id=None):
        return db_session.query(PostModel).filter_by(id=post_id).first()


    def resolve_comment_by_id(self, info, comment_id=None):
        return db_session.query(CommentModel).filter_by(id=comment_id).first()

class Mutation(graphene.ObjectType):
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
