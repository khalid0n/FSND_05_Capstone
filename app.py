from models import setup_db, Movie, Actor
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS

app = Flask(__name__)
setup_db(app)
CORS(app, resources={"/": {"origins": "*"}})


