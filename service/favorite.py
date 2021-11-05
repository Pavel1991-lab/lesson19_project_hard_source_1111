
from dao.favorite_ import FavoriteDAO


class FavoriteService:
    def __init__(self, dao: FavoriteDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, favorite_d):
        return self.dao.create(favorite_d)

    def update(self, favorite_d):
        self.dao.update(favorite_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)