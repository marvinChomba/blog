from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):

    # create instance of Flask
    app = Flask(__name__)

    # add configurations
    app.config.from_object(config_options[config_name])

    # initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app