from application.dao.model.directors import Director


class DirectorDAO:
    """Объект доступа к данным для directors модели."""
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """Метод для получения одного режиссера по ID."""
        return self.session.query(Director).get(did)

    def get_all(self):
        """Метод для получения всех режиссеров."""
        return self.session.query(Director).all()
