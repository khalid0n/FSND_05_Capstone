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
        formatted_actors = [actor.format() for actor in actors]

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
        formatted_movies = [movie.format() for movie in movies]

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
@app.route('/actors', methods=['POST'])
def add_actors():
    try:
        body = request.get_json()

        new_name = body.get('name', None)
        new_gender = body.get('gender', None)
        new_age = body.get('age', None)

        actor = Actor(name=new_name, age=new_age, gender=new_gender)
        actor.insert()

        return jsonify({
            'success': True,
            'created': actor.id,
            'actor_name': actor.name,
            'age': actor.age,
            'gender': actor.gender
        })

    except:
        traceback.print_exc()
        abort(422)

# @TODO POST Movies
@app.route('/movies', methods=['POST'])
def add_movies():
    try:
        body = request.get_json()

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        movie = Movie(title=new_title, release_date=new_release_date)
        movie.insert()

        return jsonify({
            'success': True,
            'created': movie.id,
            'movie_title': movie.title,
            'release_date': movie.release_date
        })

    except:
        traceback.print_exc()
        abort(422)


# @TODO PATCH Actors
@app.route('/actors/<int:id>', methods=['PATCH'])
def update_actors(id):
    try:
        body = request.get_json()
        actor = Actor.query.filter_by(id=id).one_or_none()

        if actor is None:
            abort(404)

        new_name = body.get('name', None)
        new_gender = body.get('gender', None)
        new_age = body.get('age', None)

        if new_name is not None:
            actor.name = new_name

        if new_gender is not None:
            actor.gender = new_gender

        if new_age is not None:
            actor.age = new_age

        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.format()
        })

    except:
        traceback.print_exc()
        abort(500)

# @TODO PATCH Movies
@app.route('/movies/<int:id>', methods=['PATCH'])
def update_movies(id):
    try:
        body = request.get_json()
        movie = Movie.query.filter_by(id=id).one_or_none()

        if movie is None:
            abort(404)

        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        if new_title is not None:
            movie.title = new_title

        if new_release_date is not None:
            movie.release_date = new_release_date

        movie.update()
        return jsonify({
            'success': True,
            'actor': movie.format()
        })

    except:
        traceback.print_exc()
        abort(500)

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

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal server error"
    }), 500
