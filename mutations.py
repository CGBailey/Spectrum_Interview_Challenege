import graphene

from .models import db_session, Posts as PostModel
from .query_types import Posts

class UpdatePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.String(required=True)
        title = graphene.String(required=False, default_value=None)
        body = graphene.String(required=False, default_value=None)
        user_id = graphene.String(required=False, default_value=None)
    u_post = graphene.Field(Posts)
    @classmethod
    def mutate(cls, root, info, post_id, title, body):
        print(post_id)
        post = db_session.query(PostModel).filter_by(id=post_id).first()
        if title is not None:
            post.title = title
        if body is not None:
            post.body = body
        
        db_session.commit()
        return UpdatePost(u_post=post)


class DeletePost(graphene.Mutation):
    class Arguments:
        post_id = graphene.String(required=True)
    d_post = graphene.Field(Posts)
    @classmethod
    def mutate(cls, root, info, post_id):
        post = db_session.query(PostModel).filter_by(id=post_id).first()
        db_session.delete(post)
        db_session.commit()

        return DeletePost(d_post=post)


