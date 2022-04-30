from os import unlink
import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    """
    Test class to test behaviour of movie class
    """

    def setUp(self):
        """
        Set up method that will run before every test
        """
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        """
        Check if instance of movie is created
        """
        self.assertTrue(isinstance(self.new_movie,Movie))

