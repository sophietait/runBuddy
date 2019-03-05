from werkzeug.utils import secure_filename

from app import app
from app import APP_EXAMPLE, ALLOWED_EXTENSIONS
from flask import request, flash, redirect
from flask import render_template
from models import run_data
import json
import os
import boto3


def allowed_file(filename: str):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/runData', methods=['GET', 'PUT'])
def rundata():
    print(request.files)
    if request.method == 'PUT':
        res = upload_run_data()
        return res
    else:
        res = get_run_data()
        return res


def get_run_data():
    requested_file = request.args.get('file', 'run1.csv')
    run1 = run_data.RunData(os.path.join(APP_EXAMPLE, requested_file))
    response = app.response_class(
        response=json.dumps(run1.get_rate()),
        status=200,
        mimetype='application/json'
    )
    return response


def upload_run_data():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    f = request.files['file']
    if f.filename == '':
        flash('No selected file')
        return redirect(request.url)
    #if f and allowed_file(f.filename):
    if f:
        filename = secure_filename(f.filename)
        full_obj_key = 'runDataFiles/{}'.format(filename)
        s3 = boto3.client('s3')
        bucket_name = os.getenv('RUNDATA_BUCKET')
        s3.upload_fileobj(f, bucket_name, full_obj_key)
        return app.response_class(status=201, response='OK')
    return app.response_class(status=500, response="error")

