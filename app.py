from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from dao.model.user import User
from implemented import user_service
from views.user import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)

app = create_app(Config())
app.debug = True

"""
with app.app_context():
    User.__table__.drop(db.engine)
    db.create_all()
    u1 = User(email="@vasya", password=user_service.make_user_password_hash("my_little_pony"), username="alex", surname="vovk", role="user", favorite_genre_id=1, favorite_movie_id=4)
    with db.session.begin():
        db.session.add_all([u1])
"""

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
