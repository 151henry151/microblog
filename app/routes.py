#!/usr/bin/env python3
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Henry'}
    return render_template('index.html', title='Home', user=user)
