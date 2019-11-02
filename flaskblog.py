from flask import Flask, render_template, url_for

APP = Flask(__name__)

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


if __name__ == '__main__':
    APP.run(debug=True)
