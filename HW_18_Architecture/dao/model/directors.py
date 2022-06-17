from setup_db import db
from marshmallow import Schema, fields


class Director(db.Model):
    __tablename__ = 'directors'
    """Модель класса режиссеров."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)


class DirectorSchema(Schema):
    """Схема для сериализации класса режиссеров."""
    id = fields.Int()
    name = fields.Str()
