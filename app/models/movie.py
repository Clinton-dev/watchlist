class Movie:
    """
    Movie class to define Movie objects
    """

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.poster = poster
        self.vote_average = vote_average
        self.vote_count = vote_count