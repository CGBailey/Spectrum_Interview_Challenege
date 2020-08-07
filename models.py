from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql:///example', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class UserAddress(Base):
    __tablename__ = 'user_addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    suite = Column(String)
    city = Column(String)
    zipcode = Column(String)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    phone = Column(String)
    website = Column(String)
    address_id = Column(Integer, ForeignKey('user_addresses.id'))
    address = relationship(
        UserAddress,
        backref=backref('users',
                        uselist=True,
                        cascade='delete,all'))

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(
            Users,
            backref=backref('posts',
                            uselist=True,
                            cascade='delete,all'))


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    body = Column(String)
    email = Column(String)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(
            Posts,
            backref=backref('comments',
                            uselist=True,
                            cascade='delete,all'))
