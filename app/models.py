class Movie:
    """
    Movie class to define Movie objects
    """

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.vote_average = vote_average
        self.vote_count = vote_count


class Review:

    all_review = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review

    def save_review(self):
        Review.all_review.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_review.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_review:
            if review.movie_id == id:
                response.append(review)


