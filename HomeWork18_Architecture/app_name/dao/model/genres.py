from app_name.setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __tablename__ = 'genres'
    """Модель класса жанров."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class GenreSchema(Schema):
    """Схема для сериализации класса жанров."""
    id = fields.Int()
    name = fields.Str()
