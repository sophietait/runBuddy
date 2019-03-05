from flask import Flask
import os

ALLOWED_EXTENSIONS = set(['.csv'])

app = Flask(__name__)
app.secret_key = "super secret key"
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
APP_EXAMPLE = os.path.join(APP_ROOT, "examples")

import routes
import models
