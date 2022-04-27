from flask import render_template
from app import app
from .request import get_movies, get_movie

@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    #print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movies, upcoming = upcoming_movies, now_showing = now_showing_movie)

@app.route('/movie/<int:id>')# <movie_id> this part is dynamic
def movie(id):
    """
     view movie page function that returns the movie details and its data
    """
    movie = get_movie(id)
    title = f'{movie.title}'
    return render_template('movie.html', title = title, movie= movie)