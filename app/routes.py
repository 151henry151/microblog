#!/usr/bin/env python3
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Henry'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Vermont!'
        },
        {
            'author': {'username': 'Suzie'},
            'body': 'The Joker movie sucked!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
