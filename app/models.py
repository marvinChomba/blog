from . import db
from flask_login import UserMixin

class User(db.Model):
    """
    Class I will use to create users
    """
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String)
    bio = db.Column(db.String)
    image = db.Column(db.String)
    posts = db.relationship("Post", backref = "user", lazy = "dynamic")

    

class Post(db.Model):
    __tablename__ = "posts"
    id  = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String)
    time = db.Column(db.String)
    comments = db.relationship("Comment",backref = "post", lazy = "dynamic")

class Comment(db.Model):
    __tablename__ = "comments"
    name = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    time = db.Column(db.String)
