from flaskblog import DB
from datetime import datetime


class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    username = DB.Column(DB.String(20), unique=True, nullable=False)
    email = DB.Column(DB.String(120), unique=True, nullable=False)
    image_file = DB.Column(DB.String(20), nullable=False, default='default.jpg')
    password = DB.Column(DB.String(60), nullable=False)
    posts = DB.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100), nullable=False)
    date_posted = DB.Column(DB.DateTime, nullable=False, default=datetime.utcnow)
    content = DB.Column(DB.Text, nullable=False)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
