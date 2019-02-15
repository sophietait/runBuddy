from flask import Flask
import os

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
APP_EXAMPLE = os.path.join(APP_ROOT, "examples")

import routes
import models
