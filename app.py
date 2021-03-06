from models import setup_db, Movie, Actor
from flask import Flask, request, jsonify, abort
import json
from flask_cors import CORS
import traceback
from auth import requires_auth, AuthError


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={"/": {"origins": "*"}})

    @app.route('/')
    def hello():
        return "HIIIIIII"

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        try:
            actors = Actor.query.order_by(Actor.id).all()
            formatted_actors = [actor.format() for actor in actors]

            return jsonify({
                'success': True,
                'actors': formatted_actors
            })

        except Exception:
            traceback.print_exc()
            abort(422)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        try:
            movies = Movie.query.order_by(Movie.id).all()
            formatted_movies = [movie.format() for movie in movies]

            return jsonify({
                'success': True,
                'actors': formatted_movies
            })

        except Exception:
            traceback.print_exc()
            abort(422)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors(jwt, id):
        try:
            actor = Actor.query.filter(Actor.id == id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()
            return jsonify({
                'success': True,
                'deleted': id
            })

        except Exception:
            traceback.print_exc()
            abort(422)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies(jwt, id):
        try:
            movie = Movie.query.filter(Movie.id == id).one_or_none()

            if movie is None:
                abort(404)

            movie.delete()
            return jsonify({
                'success': True,
                'deleted': id
            })

        except Exception:
            traceback.print_exc()
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_actors(jwt):
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

        except Exception:
            traceback.print_exc()
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_movies(jwt):
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

        except Exception:
            traceback.print_exc()
            abort(422)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actors(jwt, id):
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

        except Exception:
            traceback.print_exc()
            abort(500)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movies(jwt, id):
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

        except Exception:
            traceback.print_exc()
            abort(500)

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Un-Authorized'
        }), 401

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

    @app.errorhandler(AuthError)
    def authentication_error(error):
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error['description']
        }), error.status_code

    return app


app = create_app()
