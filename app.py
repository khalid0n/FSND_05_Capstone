from models import setup_db, Movie, Actor
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS
import traceback


# def create_app(test_config=None):
app = Flask(__name__)
setup_db(app)
CORS(app, resources={"/": {"origins": "*"}})

@app.route('/')
def hello():
    return "HIIIIIII"


# @TODO GET Actors
@app.route('/actors', methods=['GET'])
def get_actors():
    try:
        actors = Actor.query.order_by(Actor.id).all()
        formatted_actors = [actor.fomrat() for actor in actors]

        return jsonify({
            'success': True,
            'actors': formatted_actors
        })

    except:
        traceback.print_exc()
        abort(422)

# @TODO GET Movies
@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.order_by(Movie.id).all()
        formatted_movies = [movie.fomrat() for movie in movies]

        return jsonify({
            'success': True,
            'actors': formatted_movies
        })

    except:
        traceback.print_exc()
        abort(422)

# @TODO DELETE Actors
@app.route('/actors/<int:id>', methods=['DELETE'])
def delete_actors(id):
    try:
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            abort(404)

        actor.delete()
        return jsonify({
            'success': True,
            'deleted': id
        })

    except:
        traceback.print_exc()
        abort(422)

# @TODO DELETE Movies
@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movies(id):
    try:
        movie = Movie.query.filter(Movie.id == id).one_or_none()

        if movie is None:
            abort(404)

        movie.delete()
        return jsonify({
            'success': True,
            'deleted': id
        })

    except:
        traceback.print_exc()
        abort(422)

# @TODO POST Actors

# @TODO POST Movies

# @TODO PATCH Actors

# @TODO PATCH Movies

@app.errorhandler(404)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unable To Process"
    }), 422
