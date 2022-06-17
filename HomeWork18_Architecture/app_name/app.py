from flask import Flask
from flask_restx import Api

from app_name.config import Config
from app_name.setup_db import db
from app_name.views.directors import director_ns
from app_name.views.genres import genre_ns
from app_name.views.movies import movie_ns


# функция создания основного объекта app_name
def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run(host="localhost", port=10100, debug=True)
