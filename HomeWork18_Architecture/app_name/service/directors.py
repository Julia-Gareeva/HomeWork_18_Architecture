from app_name.dao.directors import DirectorDAO


class DirectorService:
    """Класс с бизнес-логикой сущности режиссеры."""
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """Метод для получения одного режиссера по ID."""
        return self.dao.get_one(did)

    def get_all(self):
        """Метод для получения всех режиссеров."""
        return self.dao.get_all()
