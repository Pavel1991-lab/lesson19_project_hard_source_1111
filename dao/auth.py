from flask import jsonify, request

from dao.model.user import User
from setup_db import db


class AuDAO:
    def __init__(self, session):
        self.session = session


    def register(self, new_user):
        data = User(**new_user)
        # проверяем, есть ли уже пользователь с таким email

        # создаем нового пользователя и сохраняем в базу данных
        db.session.add(data)
        db.session.commit()
        return data