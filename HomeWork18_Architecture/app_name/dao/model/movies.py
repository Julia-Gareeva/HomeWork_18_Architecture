from app_name.setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movies'
    """Модель класса фильмы."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), unique=True, nullable=False)
    trailer = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float, nullable=False)

    genre_id = db.Column(db.Integer, db.ForeignKey("genres.id"))
    genre = db.relationship("Genre")

    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))
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
