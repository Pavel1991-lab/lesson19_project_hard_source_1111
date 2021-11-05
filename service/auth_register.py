from dao.auth import AuDAO


class AuthRegService:
    def __init__(self, dao: AuDAO):
        self.dao = dao

    def create(self, new_user):
        return self.dao.register(new_user)