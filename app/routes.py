from flask import render_template
from app import app
from . import models
import json


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'User'}
    posts = [
        {
            'author': {'username': 'Alex'},
            'body': 'Beautiful day in San Francisco!'
        },
        {
            'author': {'username': 'CJ'},
            'body': 'The Avengers movie was cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) 


@app.route('/run1/coordinates', methods=['GET'])
def getrun1data():
    run1 = models.runData('models/examples/run2.csv')
    response = app.response_class(
        response= json.dumps(run1.getLatLong()),
        status=200,
        mimetype='application/json'
    )
    return response