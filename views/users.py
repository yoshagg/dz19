from flask_restx import Resource, Namespace
from flask import request

from models import User, UserSchema
from setup_db import db

users_ns = Namespace('users')

@users_ns.route("/users/")
class UsersView(Resource):
    def post(self):
        req_json = request.json
        ent = User(**req_json)
        db.session.add(ent)
        db.session.commit()
        return "", 201
