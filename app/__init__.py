from flask import Flask
from flask_material import Material
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
material = Material()

def create_app(config_name):

    # create instance of Flask
    app = Flask(__name__)

    # add configurations
    app.config.from_object(config_options[config_name])

    # initialize extensions
    material.init_app(app)
    db.init_app(app)

    return app