import os


class Config:
    SECRET_KEY = os.environ.get('FLASKBLOG_SECRET_KEY')
    DB_USER = os.environ.get('FLASKBLOG_DATABASE_USER')
    DB_PASSWORD = os.environ.get('FLASKBLOG_DATABASE_PASSWORD')
    DB_HOST = os.environ.get('FLASKBLOG_DATABASE_HOST')
    DB_DATABASE = os.environ.get('FLASKBLOG_DATABASE')
    DB_PORT = 5432
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FLASKBLOG_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('FLASKBLOG_EMAIL_PASS')


class DevConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'


class ProdConfig(Config):
    DEBUG = False
