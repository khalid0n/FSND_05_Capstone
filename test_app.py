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

        self.casAssist = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzUxNmVhM2ZjNzAwNzg3NmMxMGYiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4NTc5NTcwLCJleHAiOjE2MDg1ODY3NzAsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.HszmfPtTuVCoeaiVSGMrT8t9qLP4HKrvHF9h2gQLH4aIOh3otcYkfyLtCnbp6guM3vULzXHn2pTmdjedSQiIo3pjbB8HzsuRr09qH2Y06adC1vQg3LSFNjsl_dJiu-6f2uhbCF4A8si7Oj9oglQaLz6x_whlCtn7ElapVw_CrlFMA_QDBhqZcBQKwrkGWeTW-KBpPglHcXyPMm1Ejq2BeuS8_cbuiPHyEo3EHhNDryBAhCNyPVibv0D5Cjk-ycwb7mn-6vkAzeAftO-coCcdCMvinLVT3uPwRVuvdvnq45hk0FwREOKxCq3UO_cnoSxIZHLhaGPCWTgSRoyenVMJBQ'
        self.casDir = ''
        self.exec = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU2YTA4Mjg0YjAwNmJiNGM4M2UiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4NTc5OTg1LCJleHAiOjE2MDg1ODcxODUsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.C3gm7hQkIQHZD5mPX-16zJA98OklcG6oig-I532vKrcPioHd2V9mWN-Mjm6pyK06pDpfqFfAAaJr5xEzOW35tIo1AluDDZRPs6dEs7vpgg4918pbWjqRWCbcVREMQR6RGkttZlRxQ9867pgztHvXjH9-pVVBAxgcZMWcPm_woWOvOgHdyJwyj1aF2Dp9ovX_d6pUugPCcEIuKtUctU0rSeqwnjqE4iPI-iV91nvRvUZ8PpNIMrFwEQDPA-x2eZi0kB63ERFD1XcS6TETFmmZkBwkDHsW90XTWUJMxnKmxU4pqzurgg5FG3gE41vK_RzVVV_7JwNzwTNcrvCZhPIQmw'

    def tearDown(self):
        pass

    # ===================SUCCESS=========================
    def test_get_actors(self):
        response = self.client().get('/actors', headers={'Authorization': 'Bearer ' + self.casAssist})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO GET Movies
    def test_get_movies(self):
        response = self.client().get('/movies', headers={'Authorization': 'Bearer ' + self.casAssist})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO DELETE Actors
    def test_delete_actor(self):
        response = self.client().delete('/actors/1', headers={'Authorization': 'Bearer ' + self.exec})
        data = json.loads(response.data)

        actor = Actor.query.filter(Actor.id == 1).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertEqual(actor, None)

    # @TODO DELETE Movies
    def test_delete_movie(self):
        response = self.client().delete('/movies/1', headers={'Authorization': 'Bearer ' + self.exec})
        data = json.loads(response.data)

        movie = Movie.query.filter(Movie.id == 1).one_or_none()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertEqual(movie, None)

    # @TODO POST Actors
    def test_post_actor(self):
        response = self.client().post('/actors', json=self.new_actor, headers={'Authorization': 'Bearer ' + self.exec})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO POST Movies
    def test_post_movie(self):
        response = self.client().post('/movies', json=self.new_movie, headers={'Authorization': 'Bearer ' + self.exec})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO PATCH Actors
    def test_update_actor(self):
        response = self.client().patch('/actors/2', json=self.new_actor, headers={'Authorization': 'Bearer ' + self.exec})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # @TODO PATCH Movies
    def test_update_movie(self):
        response = self.client().patch('/movies/4', json=self.new_movie, headers={'Authorization': 'Bearer ' + self.exec})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


# ===================Failure=========================
# @TODO GET Actors


# @TODO GET Movies


# @TODO DELETE Actors


# @TODO DELETE Movies


# @TODO POST Actors


# @TODO POST Movies


# @TODO PATCH Actors


# @TODO PATCH Movies


# ===================Failure=========================
# @TODO Casting Assistant 2 Tests


# @TODO Casting Director 2 Tests


# @TODO Executive Assistant 2 Tests


if __name__ == "__main__":
    unittest.main()
