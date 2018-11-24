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

    def get_user_posts(self):
        posts = Post.query.filter_by(user_id = self.id)
        return posts
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Post(db.Model):
    __tablename__ = "posts"
    id  = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    content = db.Column(db.String)
    time = db.Column(db.String)
    comments = db.relationship("Comment",backref = "post", lazy = "dynamic")

    def get_post_comments(self):
        return Comment.query.filter_by(post_id = self.id)

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    title = db.Column(db.String)
    content = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    time = db.Column(db.String)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
