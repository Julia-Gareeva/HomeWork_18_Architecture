from application.dao.genres import GenreDAO


class GenreService:
    """Класс с бизнес-логикой сущности жанры."""
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        """Метод для получения одного жанра по ID."""
        return self.dao.get_one(gid)

    def get_all(self):
        """Метод для получения всех жанров."""
        return self.dao.get_all()
