from distutils.debug import DEBUG


class Config:
    """
    General config parent class
    """
    MOVIE_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

class ProdConfig(Config):
    """
    Production config child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    """
    DEBUG = True