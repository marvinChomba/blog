from . import main
from flask_login import current_user, login_required
from .forms import AddPostForm
from ..models import Post,User,Comment
from flask import redirect,url_for,render_template
@main.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html",posts = posts)

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

