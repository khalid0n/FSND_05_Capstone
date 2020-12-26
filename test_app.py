import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor
import os


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstoneDB1"
        self.database_path = "postgres://{}@{}/{}".\
            format('khalednasser', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.new_actor = {
            "name": "Mouth",
            "age": 22,
            "gender": "M"
        }

        self.new_movie = {
            "title": "Inception2",
            "release_date": "2010-10"
        }

        self.castingAssistantToken = os.environ.get('Assistant')
        self.castingDirectorToken = os.environ.get('Director')
        self.ExecutiveToken = os.environ.get('Executive')

    def tearDown(self):
        pass

    # ===================SUCCESS=========================
    def test_get_actors(self):
        response = self.client().get(
            '/actors',
            headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_get_movies(self):
        response = self.client().get(
            '/movies',
            headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        response = self.client().delete(
            '/actors/6',
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)

        actor = Actor.query.filter(Actor.id == 6).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)
        self.assertEqual(actor, None)

    def test_delete_movie(self):
        response = self.client().delete(
            '/movies/7',
            headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)

        movie = Movie.query.filter(Movie.id == 7).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 7)
        self.assertEqual(movie, None)

    def test_post_actor(self):
        response = self.client().post(
            '/actors', json=self.new_actor,
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movie(self):
        response = self.client().post(
            '/movies', json=self.new_movie,
            headers={'Authorization': 'Bearer ' + self.ExecutiveToken})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor(self):
        response = self.client().patch(
            '/actors/2',
            json=self.new_actor,
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie(self):
        response = self.client().patch(
            '/movies/4',
            json=self.new_movie,
            headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # ===================failure=========================
    def test_fail_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    def test_fail_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    def test_fail_delete_actor(self):
        response = self.client().delete('/actors/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    def test_fail_delete_movie(self):
        response = self.client().delete('/movies/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    def test_fail_post_actor(self):
        response = self.client().post(
            '/actors',
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unable To Process")

    def test_fail_post_movie(self):
        response = self.client().post(
            '/movies',
            headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unable To Process")

    def test_fail_update_actor(self):
        response = self.client().patch(
            '/actors/2',
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Internal server error")

    def test_fail_update_movie(self):
        response = self.client().patch(
            '/movies/4',
            headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Internal server error")

    # ===================RBAC Test=========================
    def test_assistant_post_actor(self):
        response = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")

    def test_assistant_delete_actor(self):
        response = self.client().delete(
            '/actors/1',
            headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")

    def test_Director_post_movie(self):
        response = self.client().post(
            '/movies', json=self.new_movie,
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")

    def test_Director_delete_movie(self):
        response = self.client().delete(
            '/movies/1',
            headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")


if __name__ == "__main__":
    unittest.main()
