from flask import request
from flask_restx import Resource, Namespace
from utils import auth_required, admin_required
from dao.model.movie import MovieSchema
from implemented import favorite_service

favorite_ns = Namespace('favorite')


@favorite_ns.route('/')
class MoviesView(Resource):

    def post(self):
        req_json = request.json
        favorite_service.create(req_json)
        return "", 201