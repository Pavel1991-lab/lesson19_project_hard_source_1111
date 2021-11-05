from marshmallow import Schema, fields

from setup_db import db


class Favorite_genre(db.Model):
    __tablename__ = 'faivorite_genre'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))


class Favorite_genreSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    movie_id = fields.Int()
