# файл для создания DAO и сервисов чтобы импортировать их везде
from application.dao.directors import DirectorDAO
from application.dao.genres import GenreDAO
from application.dao.movies import MovieDAO
from application.service.directors import DirectorService
from application.service.genres import GenreService
from application.service.movies import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)