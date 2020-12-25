import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstoneDB1"
        self.database_path = "postgres://{}@{}/{}".format('khalednasser', 'localhost:5432', self.database_name)
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

        self.castingAssistantToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzUxNmVhM2ZjNzAwNzg3NmMxMGYiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4OTEwMTc5LCJleHAiOjE2MDg5MTczNzksImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.EiNhLbBLcOwQAdCIeyC89N0ST2UOy8qTTyNCGkydYSL_VW0AmGftG30NhhqTr44ZzQdg0wAp3bS3yd24-5wEif02C5_M0KxS5WNHcNzCgDH33LW5DZOdgvPkzsOW62hxmjoevdm34pivDCEuVODFHtCf8BAYPqZodPJuq0GFT-OD5-SViMvN5rltcbcj94DvDDFRqiAdSmGC7yvDCsS4C2ZE79dMJLU0IxgNz27a3Mh7M5l0s-VRDDIoF1yAIwMnRs7jgQu5NlfqeLDUfFRdpqvxSpv6m7k6vohLBDd9jQgD-5gcKjUk4MqH3IjqXN6bTnbcy9j-GPtSY5SLa2sumg'
        self.castingDirectorToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU0Yjc4MjM4YjAwNzE5NjVhYmQiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4OTEwMjIzLCJleHAiOjE2MDg5MTc0MjMsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.lcmqWaUV0ODpDrlDSO08MEpAmr1LsbSkeWT9ZOYY0_YO1F0uV1nI9ZC0gs1ZnVc7Es53WxefbQEN9u4XvgemXch8epFrQF40Sgf_MDD_4amT7dFFlYsay_CpaT2S125WofRUmX7efHwD9EbH2JEygylNodiq9xJ8ZF4Eq5BKblUDfSbM93IIIFw4sXIHPHXpatcKGMuV7kkgSNgeQ0AvAEYsoZyTEpoRMDSvwWI-Gaq4jJFLrXucgRCowAM1aHHmvUhiXnlRzJ25nbVV7GN7FSYztHwJ8aSDE-0fzuyzke2XVpTYIdCwC3Ig3X3Pf8d0M0fvo_fmhs037oQpuSbydw'
        self.ExecutiveToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU2YTA4Mjg0YjAwNmJiNGM4M2UiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4OTEwMjUzLCJleHAiOjE2MDg5MTc0NTMsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.kLtlPK5RbFA3jOtNHOqKcWzpmY8KyO0psV2G27yeG54wQAkhvGUFjS81ZLa0f25UO8-IepIwxBj4BU68UPjQRTO6Nvqak8_bJXSxF5nJP-Lqq-Su7pSxnbVZpmw9AjeAh5dImofiPqGQZLXnUDH3nfts6ijET02WMIbJhGwBYHFQy95RkDadGLhROYKlEuYI16wnq1VbtrEbRXZPRaIZKZiVRbk9-mTXs5jlWsvpfjO7BEKfCwrWM8GZ6mh4TKpotI1v0578ZfwkEilgTELQ6HQfDFjooy5oAEodIQOF5M2QapeUodupBjLrQAjadat4b3i1eZQQOFZEr-YOOIgozQ'

    def tearDown(self):
        pass

    # ===================SUCCESS=========================
    def test_get_actors(self):
        response = self.client().get('/actors', headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO GET Movies
    def test_get_movies(self):
        response = self.client().get('/movies', headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO DELETE Actors
    def test_delete_actor(self):
        response = self.client().delete('/actors/6', headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)

        actor = Actor.query.filter(Actor.id == 6).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 6)
        self.assertEqual(actor, None)

    # @TODO DELETE Movies
    def test_delete_movie(self):
        response = self.client().delete('/movies/7', headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)

        movie = Movie.query.filter(Movie.id == 7).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 7)
        self.assertEqual(movie, None)

    # @TODO POST Actors

    def test_post_actor(self):
        response = self.client().post('/actors', json=self.new_actor,
                                      headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO POST Movies
    def test_post_movie(self):
        response = self.client().post('/movies', json=self.new_movie,
                                      headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO PATCH Actors
    def test_update_actor(self):
        response = self.client().patch('/actors/2', json=self.new_actor,
                                       headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO PATCH Movies
    def test_update_movie(self):
        response = self.client().patch('/movies/4', json=self.new_movie,
                                       headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # ===================failure=========================
    # @TODO GET Actors
    def test_fail_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    # @TODO GET Movies
    def test_fail_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    # @TODO DELETE Actors
    def test_fail_delete_actor(self):
        response = self.client().delete('/actors/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    # @TODO DELETE Movies
    def test_fail_delete_movie(self):
        response = self.client().delete('/movies/1')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Authorization header is expected")

    # @TODO POST Actors
    def test_fail_post_actor(self):
        response = self.client().post('/actors', headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unable To Process")

    # @TODO POST Movies
    def test_fail_post_movie(self):
        response = self.client().post('/movies', headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unable To Process")

    # @TODO PATCH Actors
    def test_fail_update_actor(self):
        response = self.client().patch('/actors/2', headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Internal server error")

    # @TODO PATCH Movies
    def test_fail_update_movie(self):
        response = self.client().patch('/movies/4', headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Internal server error")

    # ===================RBAC Test=========================
    # @TODO Casting Assistant 2 Tests
    def test_assistant_post_actor(self):
        response = self.client().post('/actors', json=self.new_actor,
                                      headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")

    def test_assistant_delete_actor(self):
        response = self.client().delete('/actors/1', headers={'Authorization': 'Bearer ' + self.castingAssistantToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")

    # @TODO Casting Director 2 Tests
    def test_Director_post_movie(self):
        response = self.client().post('/movies', json=self.new_movie,
                                      headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")

    def test_Director_delete_movie(self):
        response = self.client().delete('/movies/1', headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permissions not found")


if __name__ == "__main__":
    unittest.main()
