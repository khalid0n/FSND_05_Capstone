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
            "name": "Khaled",
            "age": 33,
            "gender": "M"
        }

        self.new_movie = {
            "title": "Inception",
            "release_date": "2010-10"
        }

    def tearDown(self):
        pass

#===================SUCCESS=========================
    # @TODO GET Actors


    # @TODO GET Movies


    # @TODO DELETE Actors


    # @TODO DELETE Movies


    # @TODO POST Actors


    # @TODO POST Movies


    # @TODO PATCH Actors


    # @TODO PATCH Movies


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



