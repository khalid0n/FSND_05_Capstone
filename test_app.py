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

        self.castingAssistantToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzUxNmVhM2ZjNzAwNzg3NmMxMGYiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4OTI5OTY1LCJleHAiOjE2MDkwMTYzNjUsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ZBmV7Tc0H6Io78Pt4iL94O36cuigDxnpbLWdFzZWeLFdmgaICxBeEJRNbjRJIM6oXHopYWbnCJedM9wrG-cBbgmCNP-w8c2D437S88V425-PoziuPwfj5jN4JgQMqhzZCSHc-3aLLULjUrR5Nkepbsh8uzbiZZ65jXHIGX8V3zECLg_Hxs7oYaNltNX8I9OKe0qbWFAHM--Z_HCBWrj66hRi_qgpxzfqDAY7SQ1NlPP5ATsAgiN_sYPY17ZJWTGij8dpSuKVXpkep3_5I5lgIbiyti1cGzcfVh_LC-7GQX_8Xhq8lBwQfVNTBod82s_vI-jFaxW3yYGirsnQBluS7g'
        self.castingDirectorToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU0Yjc4MjM4YjAwNzE5NjVhYmQiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4OTI5OTMwLCJleHAiOjE2MDkwMTYzMzAsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.AX7-ZeG9_XJEJonn8QkFB5-3Zxk-Ll6EE4nMwuRSj9NtBTqiIQpZ0lFe0thNWhdughxvcNJl4pJh_b5Y5w1Hyh7OwsmuTWkDmWybMOT48JoyVWz_tjo61q5u88uKru0Ed2KQdg2i8t85T03jiXhnBaEGFI2qt3sGELxA1hrd-gojGfIB9qhwt8kQ01kTrjKlZkSbS17iDtcTw3fIHgNmZUkxc8BtrgGTpbTFTFBLtpnXZpNKobs-3zI1yqcxWH1SHbjJzVc8mDWzFKSxJDNjPdd5VND9ImTa6_nAwGJri2OBrL4JIeyeFWgsZ11UA3t9gWofYkFWS_hPHVhHIO9StA'
        self.ExecutiveToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImlDcllNXzdYc0JMVVBucVZnT2xWZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmQta2hhbGVkLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmRmNzU2YTA4Mjg0YjAwNmJiNGM4M2UiLCJhdWQiOiJmbnNkX2NhcHN0b25lIiwiaWF0IjoxNjA4OTI5OTAzLCJleHAiOjE2MDkwMTYzMDMsImF6cCI6IkxndU52NE9Qajd0V05lMW92MTJ1WmppT0xvUW54SndRIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.dy9SUsVu1rzW6ww0_9fHSjW5WoLKmlu_q4OH_BOHcW6TrTnV7LkhHthA2OGlJhPnGxJOCKI5Ul0zlBQGaZ9bukk7JiR3niuQ05FdViF9OWqY7g4p1ShxaQ63rbky6-oQC_IoJfQK6U2WObh3I_f4aFhsNHlUH9n0qRCyg-1yG2NWQ2KYo1xrZtUcT4Ul7F1b5y-8xEo82UB5Y6gvn7YIvwyukXQizbl5pC7qmAL23axyxoa09fjqR1ocOOro0owzg4WcOPJ-0LfZ_CUMbhjJbmURQn6SPoHZ4tBjR15hai7kc82ZWZGYNUHwRzQgAYbZnkYJhjCz6QDiw1bExXc0Kg'

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
