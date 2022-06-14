# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
api.app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')

###___________________________________________________________________________________________


class Movie(db.Model):
    __tablename__ = 'movie'
    """Модель класса фильмы."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    trailer = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    """Схема для сериализации класса фильмы."""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()

###_________________________________________________________________________________


class Director(db.Model):
    __tablename__ = 'director'
    """Модель класса режиссеров."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    """Схема для сериализации класса режиссеров."""
    id = fields.Int()
    name = fields.Str()

###____________________________________________________________________________________


class Genre(db.Model):
    __tablename__ = 'genre'
    """Модель класса жанров."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class GenreSchema(Schema):
    """Схема для сериализации класса жанров."""
    id = fields.Int()
    name = fields.Str()

###____________________________________________________________________________


"""Здесь регистрируем класс (Class-Based View) по пути /movies/ (эндпоинту)."""
@movies_ns.route('/')
class MovieView(Resource):
    def get(self):
        """Получение списка фильмов."""
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        # Условие при котором будут возвращаться режиссеры/жанры по ID, или и те и другие по ID.
        movies = Movie.query
        if director_id:
            movies = movies.filter(Movie.director_id == director_id)
        if genre_id:
            movies = movies.filter(Movie.genre_id == genre_id)

        movies = movies.all()
        return MovieSchema(many=True).dump(movies), 200

    def post(self):
        """Создание фильма, здесь мы получаем данные из запроса и создаем новую сущность в БД."""
        data = request.get_json()
        new_movie = Movie(**data)
        db.session.add(new_movie)
        db.session.commit()
        db.session.close()
        return "", 201


@movies_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        """Получение конкретного фильма по идентификатору."""
        movie = Movie.query.get(mid)
        return MovieSchema().dump(movie), 200

    def put(self, mid):
        """Обновление фильма по идентификатору."""
        data = request.get_json()
        movie = Movie.query.get(mid)
        movie.title = data['title']
        movie.description = data['description']
        movie.trailer = data['trailer']
        movie.year = data['year']
        movie.rating = data['rating']
        movie.genre_id = data['genre_id']
        movie.director_id = data['director_id']

        db.session.add(movie)
        db.session.commit()
        db.session.close()
        return "", 204

        # movie = db.session.query(Movie).get(mid)
        # req_json = request.json

        # movie.title = req_json.get('title')
        # movie.description = req_json.get('description')
        # movie.trailer = req_json.get('trailer')
        # movie.year = req_json.get('year')
        # movie.rating = req_json.get('rating')
        # movie.genre_id = req_json.get('genre_id')
        # movie.director_id = req_json.get('director_id')
        # db.session.add(movie)
        # db.session.commit()
        # return "", 204

    def patch(self, mid):
        """Частичное обновление фильма."""
        movie = Movie.query.get(mid)
        req_json = request.json
        if "title" in req_json:
            movie.title = req_json.get("title")
        if "description" in req_json:
            movie.description = req_json.get("description")
        if "trailer" in req_json:
            movie.trailer = req_json.get("trailer")
        if "year" in req_json:
            movie.year = req_json.get("year")
        if "rating" in req_json:
            movie.rating = req_json.get("rating")
        if "genre_id" in req_json:
            movie.genre_id = req_json.get("genre_id")
        if "director_id" in req_json:
            movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, mid):
        """Удаление фильма"""
        movie = Movie.query.get(mid)
        db.session.delete(movie)
        db.session.commit()
        return "", 204


if __name__ == '__main__':
    app.run(debug=True)
