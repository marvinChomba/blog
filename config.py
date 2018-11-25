import os

class Config:
    """
    This is the class which will contain the general configurations
    """
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = "app/static/photos"

class DevConfig(Config):
    """
    This is the class which will contain the development configurations
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marvin:marvin24@localhost/blog'
    DEBUG = True

class ProdConfig(Config):
    """
    This is the class which will contain the production configurations
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    """
    This is the class which will contain the test configurations
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://marvin:marvin24@localhost/tests'

config_options = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig
}


