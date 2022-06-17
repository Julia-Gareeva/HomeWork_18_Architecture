from app_name.dao.movies import MovieDAO


class MovieService:
    """Класс с бизнес-логикой сущности фильмы."""
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        """Метод для получения одного фильма по ID."""
        return self.dao.get_one(mid)

    def get_all(self):
        """Метод для получения всех фильмов."""
        return self.dao.get_all()

    def get_directors_id(self, mid):
        """Метод для получения фильмов с определенным режиссером по запросу типа /movies/?director_id=14"""
        return self.dao.get_directors_id(mid)

    def get_genre_id(self, mid):
        """Метод для получения фильмов с определенным жанром по запросу типа /movies/?genre_id=10"""
        return self.dao.get_genre_id(mid)

    def get_year_movie(self, year):
        """Метод для получения фильмов за определенный год по запросу типа /movies?year=2007"""
        return self.dao.get_year_movie(year)

    def create(self, data):
        """Метод для создания/добавления одного фильма."""
        return self.dao.create(data)

    def update(self, data):
        """Метод для обновления одного фильма."""
        mid = data.get("id")
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def update_partial(self, data):
        """Метод для частичного обновления одного фильма."""
        mid = data.get("id")
        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')
        self.dao.update(movie)

    def delete(self, mid):
        """Метод для удаления одного фильма."""
        self.dao.delete(mid)
