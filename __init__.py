import json

from datetime import datetime

from flask import Flask, jsonify, render_template, Response
from flask_restful import Api, Resource
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)
app.config.from_object("settings.local")