from app_name.dao.model.movies import Movie


# CRUD - это набор операций: создание, чтение, обновление и удаление.
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.comit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, mid):
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
