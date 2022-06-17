from flask_restx import Resource, Namespace
from app_name.dao.model.directors import DirectorSchema
from app_name.implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        try:
            all_directors = director_service.get_all()
            return directors_schema.dump(all_directors), 200
        except Exception as ex:
            return ex, 404


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as ex:
            return ex, 404
