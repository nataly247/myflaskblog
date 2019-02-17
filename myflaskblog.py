from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Nataly Pan',
        'date_posted': 'Fabruary 17, 2019',
        'title': 'Blog Post 1',
        'content': 'First post content'
    },
    {
        'author': 'James Bond',
        'date_posted': 'Fabruary 18, 2019',
        'title': 'Blog Post 2',
        'content': 'Second post content'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')
