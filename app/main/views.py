from . import main
from flask_login import current_user, login_required
from .forms import AddPostForm,SubscribeForm
from ..models import Post,User,Comment,Subscriber
from flask import redirect,url_for,render_template,flash
from .. import db

@main.route("/", methods = ["GET","POST"])
def index():
    form = SubscribeForm()
    if form.validate_on_submit():
        email = form.email.data
        new_subscriber = Subscriber(email = email)
        db.session.add(new_subscriber)
        db.session.commit()
        flash("Thank You for subscribing!")
        return redirect(url_for("main.index"))
    posts = Post.query.all()
    return render_template("index.html",posts = posts,form = form)

@main.route("/add/post/",methods = ["GET","POST"])
@login_required
def add_post():
    form = AddPostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_post = Post(title = title, content = content, user = current_user)
        new_post.save_post()
        return redirect(url_for('main.index'))

    return render_template("add_pitch.html",form = form)

@main.route("/post/<int:id>")
def post_page(id):
    post = Post.query.filter_by(id = id).first()
    title = post.title
    return render_template("post.html", title = title, post = post)

