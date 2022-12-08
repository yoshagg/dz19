from flask_restx import Resource, Namespace
from flask import request, abort

import hashlib
import jwt

from constants import JWT_ALGORITHM as algo
from constants import JWT_SECRET as secret

from models import User, generate_tokens
from setup_db import db

auth_ns = Namespace()


@auth_ns.route('/auth')
class AuthView(Resource):
    def post(self):
        # TODO напишите Ваш код здесь
        req_json = request.json
        username = req_json.get("username", None)
        password = req_json.get("password", None)

        if None in [username, password]:
            abort(400)

        user = db.session.query(User).filter(User.username == username).first()

        if user is None:
            return {"error": "Неверные учётные данные"}, 401

        password_hash = hashlib.md5(password.encode('utf-8')).hexdigest()

        if password_hash != user.password:
            return {"error": "Неверные учётные данные"}, 401

        data = {
            "username": user.username,
            "role": user.role
        }

        tokens = generate_tokens(data)

        return tokens, 201


    def put(self):
        # TODO напишите Ваш код здесь
        req_json = request.json
        refresh_token = req_json.get("refresh_token")

        if refresh_token is None:
            abort(400)

        try:
            data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        except:
            abort(400)

        username = data.get('username')

        user = db.session.query(User).filter(User.username == username).first()

        data = {
            "username": user.username,
            "role": user.role
        }

        tokens = generate_tokens(data)

        return tokens, 201
