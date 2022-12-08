from flask_restx import Resource, Namespace
from flask import request

from models import User, get_hash, generate_password
from setup_db import db

authorization_ns = Namespace()


@authorization_ns.route('/auth')
class AuthViews(Resource):
    def post(self):
        req_json = request.json
        entered_login = req_json.get('username')
        entered_password = req_json.get('password')
        password = generate_password(entered_password)
        registered_accounts = User.query.get_all('username')
        try:
            if entered_login in registered_accounts:




    def put(self, rid):
        director = Director.query.get(rid)
        req_json = request.json
        director.name = req_json.get('name')

        db.session.add(director)
        db.session.commit()
        return "", 204
