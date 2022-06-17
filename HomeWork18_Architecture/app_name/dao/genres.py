from app_name.dao.model.genres import Genre


class GenreDAO:
    """Объект доступа к данным для genres модели."""
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        """Метод для получения одного жанра по ID."""
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """Метод для получения всех жанров."""
        return self.session.query(Genre).all()
