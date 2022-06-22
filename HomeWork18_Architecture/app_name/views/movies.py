from flask import request, jsonify
from flask_restx import Resource, Namespace
from app_name.dao.model.movies import MovieSchema
from app_name.implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


"""Представления для сущности фильмы /movies/."""
@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Метод для получения всех фильмов."""
        year_movie = request.args.get("year")
        movies = request.args.get("movies")

        try:
            if movies:
                all_movies = movie_service.get_all(movies)
                return movies_schema.dump(all_movies), 200
            if year_movie:
                all_year_movie = movie_service.get_year_movie(year_movie)
                return movies_schema.dump(all_year_movie), 200
        except Exception as Not_Found:
            return Not_Found, 404

    def post(self):
        """Метод для добавления фильма."""
        req_json = request.json
        movie_service.create(req_json)
        movies_id = req_json['pk']  # Заголовок Location в POST на создание сущности.
        response = jsonify()
        response.status_code = 201
        response.headers["location"] = f'/{movies_id}'
        return response

        # return "", 201


"""Представления для сущности фильмы /movies/<int:mid>."""
@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        """Метод для получения одного фильма по его ID."""
        directors_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        movie_one = request.args.get("mid")

        try:
            if movie_one:
                movie = movie_service.get_one(movie_one)
                return movie_schema.dump(movie), 200
            if directors_id:
                movie_dir = movie_service.get_directors_id(directors_id)
                return movie_schema.dump(movie_dir), 200
            if genre_id:
                movie_genre = movie_service.get_genre_id(genre_id)
                return movie_schema.dump(movie_genre), 200
        except Exception as Not_Found:
            return Not_Found, 404

    def put(self, mid: int):
        """Метод для изменения одного фильма по его ID."""
        req_json = request.json
        req_json["id"] = mid
        movie_service.update(req_json)

        return "", 204

    def patch(self, mid: int):
        """Метод для частичного изменения одного фильма по его ID."""
        req_json = request.json
        req_json["id"] = mid
        movie_service.update_partial(req_json)

        return "", 204

    def delete(self, mid: int):
        """Метод для удаления одного фильма по его ID."""
        movie_service.delete(mid)

        return "", 204

