from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'c653233b9d1669785d0360758cfc01e0'
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
DB = SQLAlchemy(APP)

from flaskblog import routes
