from models import setup_db, Movie, Actor
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={"/": {"origins": "*"}})



# @TODO GET Actors


# @TODO GET Movies


# @TODO DELETE Actors


# @TODO DELETE Movies


# @TODO POST Actors


# @TODO POST Movies


# @TODO PATCH Actors


# @TODO PATCH Movies




