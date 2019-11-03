from flask import render_template, url_for, flash, redirect
from flaskblog import APP
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

'''
python >>>
>>> from flaskblog import DB
>>> from flaskblog.models import User, Post
>>> DB.create_all()
>>> User.query.all() -> return []
'''
# temp data
POSTS = [
    {
        'author': 'Wojciech Gałecki',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 01, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 20, 2019'
    }
]


@APP.route("/")
@APP.route("/home")
def home():
    return render_template('home.html', posts=POSTS)


@APP.route("/about")
def about():
    return render_template('about.html', title='About')


@APP.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Successfully created account for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@APP.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Invalid username or password!', 'danger')
    return render_template('login.html', title='Login', form=form)
