import sqlalchemy
import requests
from .models import db_session, UserAddress, Users, Posts, Comments

def seed():
    users_res = requests.get('https://jsonplaceholder.typicode.com/users')
    users_json = users_res.json()

    for user in users_json:
        new_address = UserAddress()
        new_address.street = user['address']['street']
        new_address.suite = user['address']['suite']
        new_address.city = user['address']['city']
        new_address.zipcode = user['address']['zipcode']
        db_session.add(new_address)
        db_session.commit()

        new_user = Users()
        new_user.id = user['id']
        new_user.name = user['name']
        new_user.username = user['username']
        new_user.email = user['email']
        new_user.phone = user['phone']
        new_user.website = user['website']
        new_user.new_address = new_address.id
        db_session.add(new_user)
        db_session.commit()


    posts_res = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts_json = posts_res.json()

    for post in posts_json:
        print(post)
        new_post = Posts()
        new_post.id = post['id']
        new_post.title = post['title']
        new_post.body = post['body']
        new_post.user_id = post['userId']

        db_session.add(new_post)
        db_session.commit()
    comments_res = requests.get('https://jsonplaceholder.typicode.com/comments')
    comments_json = comments_res.json()

    for comment in comments_json:
        new_comment = Comments()
        new_comment.id = comment['id']
        new_comment.name = comment['name']
        new_comment.body = comment['body']
        new_comment.email = comment['email']
        new_comment.post_id = comment['postId']

        db_session.add(new_comment)
        db_session.commit()


if len(db_session.query(Comments).all()) <= 1:
    seed()
else:
    print("Comments Table has been seeded")
