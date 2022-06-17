from flask_restx import Resource, Namespace
from app_name.dao.model.genres import GenreSchema
from app_name.implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        try:
            all_genres = genre_service.get_all()
            return genres_schema.dump(all_genres), 200
        except Exception as ex:
            return ex, 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as ex:
            return ex, 404
