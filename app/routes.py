from app import app
from app import APP_EXAMPLE
from flask import request
from models import run_data
import json
import os

@app.route('/')
@app.route('/index')
def index():
    return "hello"


@app.route('/runData', methods=['GET'])
def get_run_data():
    requested_file = request.args.get('file')
    run1 = run_data.RunData(os.path.join(APP_EXAMPLE, requested_file))
    response = app.response_class(
        response=json.dumps(run1.get_rate()),
        status=200,
        mimetype='application/json'
    )
    return response
