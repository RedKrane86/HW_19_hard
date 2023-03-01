from flask import request

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        stmt = Movie.query
        if director_id:
            stmt = stmt.filter(Movie.director_id == director_id)
        if genre_id:
            stmt = stmt.filter(Movie.genre_id == genre_id)
        if year:
            stmt = stmt.filter(Movie.year == year)
        movies = stmt.all()
        return movies

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
