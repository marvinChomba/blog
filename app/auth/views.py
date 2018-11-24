from . import auth
from flask import redirect,render_template,url_for
from flask_login import login_user,logout_user
from .forms import RegistrationForm,LoginForm
from ..models import User

@auth.route("/register", methods = ["GET","POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        full_name = form.full_name.data
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = User(full_name = full_name, password = password,email = email, username = username)
        user.save_user()
        return redirect(url_for('main.index'))

    title = "Register"
    return render_template("auth/register.html", form = form)

@auth.route("/login", methods = ["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email = email).first()
        if user is not None and user.verify_pass(form.password.data):
            login_user(user,form.remember.data)
            return render_template("logged.html")
    title = "Login"
    return render_template("auth/login.html", form = form)
