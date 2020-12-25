import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        # self.database_name = "capstoneDB1"
        # self.database_path = "postgres://{}@{}/{}".format('khalednasser', 'localhost:5432', self.database_name)
        self.database_path = "postgres://ixlgpwadhntnfz:3c74f448cc176a5cf44a0536c979dd97a62ec381ba125c4543788ee3c1164f74@ec2-184-72-235-80.compute-1.amazonaws.com:5432/d9qviphab0o2hk"
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

        self.castingAssistantToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzUxNmVhM2ZjNzAwNzg3NmMxMGYiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4NzUyMzMwLCJleHAiOjE2MDg3NTk1MzAsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.CxFRZIIfT6GA-dGHdkwLcnP1Yl6to_axUDgbKHVVw7FjA1hNujhae3_LbBrK_3MglM9wSVU1L3NX1c8J1fdbZTkPoy3ypjLtqQLa1iS4nUi8WU9ew25VcstWgG120kDbTz5sx29JehjmY6q2rmILYu4eK11ASsQN_CApdGg9twbjDNIkaq1kudF7hH7uqnXN-S3bM8IqIY_Lv6v2MPhLb-B6sKvL1kW7GAeA0xiGCZHr1J7KxA6fod3iyHD6MC1YhRjigAd3p5lLgaGGlUjaZ7v-PJA4gma2sHB0SS-VB-vA49RjfwrcQhzyE1AoPCDDZzRQBV5Mzfozsw9jTcfgKQ'
        self.castingDirectorToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU0Yjc4MjM4YjAwNzE5NjVhYmQiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4NzUyMzU5LCJleHAiOjE2MDg3NTk1NTksImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.SFtxd8pe0FMx6n3GBE2UDkgpmVTagcmjGYoZuuxtGf7ErLvo4E05-1G3MGB6lbrpjKOXUURCpLpmblMOFHf25ZkNQsjbazla0jFcTTshJusexskv1EmFQVNYfS20lwdM3tQyHEovaCAaJpqYLudWn3yfbzkhBPgGz6snAOx4ZNVuf4bnuqzH8b1AcsuERKjzxAaPR3Sqd_3sT4YNc97jsr8bEmfAsQYZFCUovY-kO6WxUdQYC_yr3JqRTFd5gI5jKt8HF1XY3ogivV6JHnsQpOdWAlaxu99yU4ViLhLmnwh5ZbI_Fy5tVNAIHo1dOfRofznxK-6L9yl8-5d1NbUN-g'
        self.ExecutiveToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU2YTA4Mjg0YjAwNmJiNGM4M2UiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4NzUyNDA5LCJleHAiOjE2MDg3NTk2MDksImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.XsQNiK_GZziAFGN1uPHUNnA4codqpKQobQ9_u1aQ6-bCMUm9dFEo_og2Q_Ue4RCWUIRe0t1gbmQDb36vau484HBH0es8h2nCEle4Ak29IdfgEzMQ-4GpwbOqSyvUQR7sNhx7QuemkloUSOMDKnfmb5EOJgz4UYdwMI1U6BhJ8gBZFuELtKJCjaQj3ES49OpHs1JTLnHotfG90jrC4MIlCISZch6E9tWSpPhUlIlcaxYr9e5Xb7iZhv72S3L7v8RVpOjPDd3HLcZmAz_Ouot6pisKM3jtCANAeR59rCSsMfFanz0KrQd58F0HBQgzMGQlmMM1Ua5TWCx0HJSw36BKYw'

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
        response = self.client().delete('/actors/9', headers={'Authorization': 'Bearer ' + self.castingDirectorToken})
        data = json.loads(response.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 9)
        self.assertEqual(actor, None)

    # @TODO DELETE Movies
    def test_delete_movie(self):
        response = self.client().delete('/movies/15', headers={'Authorization': 'Bearer ' + self.ExecutiveToken})
        data = json.loads(response.data)

        movie = Movie.query.filter(Movie.id == 15).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 15)
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
