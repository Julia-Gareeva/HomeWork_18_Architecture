from flask_restx import Resource, Namespace
from setup_db import db
from dao.model.genres import Genre, GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = db.session.query(Genre).all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = db.session.query(Genre).get(gid)
        return genre_schema.dump(genre), 200
