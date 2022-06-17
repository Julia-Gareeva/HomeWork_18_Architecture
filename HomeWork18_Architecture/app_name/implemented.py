# файл для создания DAO и сервисов чтобы импортировать их везде
from app_name.dao.directors import DirectorDAO
from app_name.dao.genres import GenreDAO
from app_name.dao.movies import MovieDAO
from app_name.service.directors import DirectorService
from app_name.service.genres import GenreService
from app_name.service.movies import MovieService
from app_name.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
