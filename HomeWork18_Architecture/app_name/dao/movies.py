from app_name.dao.model.movies import Movie


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class MovieDAO:
    """Объект доступа к данным для movies модели."""
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        """Метод для получения одного фильма по ID."""
        return self.session.query(Movie).get(mid)

    def get_all(self):
        """Метод для получения всех фильмов."""
        return self.session.query(Movie).all()

    def get_directors_id(self, director_id):
        """Метод для получения фильмов с определенным режиссером по запросу типа /movies/?director_id=14"""
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_genre_id(self, genre_id):
        """Метод для получения фильмов с определенным жанром по запросу типа /movies/?genre_id=10"""
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_year_movie(self, year):
        """Метод для получения фильмов за определенный год по запросу типа /movies?year=2007"""
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data):
        """Метод для создания/добавления одного фильма."""
        movie = Movie(**data)

        self.session.add(movie)
        self.session.comit()

        return movie

    def update(self, movie):
        """Метод для обновления одного фильма."""
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
        """Метод для удаления одного фильма."""
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()


# Получить все фильмы режиссера
# Получить все фильмы жанра
# Получить все фильмы за год

# director_id = request.args.get('director_id')
# genre_id = request.args.get('genre_id')
# Условие при котором будут возвращаться режиссеры/жанры по ID, или и те и другие по ID.
# movies = Movie.query
# if director_id:
#     movies = movies.filter(Movie.director_id == director_id)
# if genre_id:
#     movies = movies.filter(Movie.genre_id == genre_id)
