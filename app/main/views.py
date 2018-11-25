from . import main
from flask_login import current_user, login_required
from .forms import AddPostForm,SubscribeForm,AddComment
from ..models import Post,User,Comment,Subscriber
from flask import redirect,url_for,render_template,flash,request
from .. import db,photos
from datetime import datetime

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
    posts = Post.query.order_by(Post.time.desc())
    return render_template("index.html",posts = posts,form = form)

@main.route("/add/post/",methods = ["GET","POST"])
@login_required
def add_post():
    form = AddPostForm()

    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        posted = str(datetime.now())
        print(posted)
        if "photo" in request.files:
            pic = photos.save(request.files["photo"])
            file_path = f"photos/{pic}"
            image = file_path
        new_post = Post(title = title, content = content, user = current_user,image = image,time = posted)
        new_post.save_post()
        return redirect(url_for('main.index'))

    return render_template("add_pitch.html",form = form)

@main.route("/post/<int:id>",methods = ["GET","POST"])
def post_page(id):
    post = Post.query.filter_by(id = id).first()
    title = post.title
    form = AddComment()
    if form.validate_on_submit():
        name = form.name.data
        content = form.comment.data
        new_comment = Comment(name = name, content = content, post = post)
        new_comment.save_comment()
        return redirect(url_for('main.post_page', id = post.id))
    comments = Comment.query.filter_by(post_id = post.id)
    return render_template("post.html", title = title, post = post,form = form,comments = comments)

