from itertools import filterfalse
import json
from flask import request, Response
from flask.json import jsonify
from system.jwt.JwtSystem import JwtSystem
from flask_pymongo import PyMongo
import hashlib

class AuthenticationController:

    def __init__(self, app):
        ###
        # POST - /login
        ###
        @app.route('/login', methods=['POST'])
        def token():
            try:
                auth = request.authorization
                password = hashlib.sha256(auth.password.encode('utf-8')).hexdigest()
                mongodb_client = PyMongo(app)
                db = mongodb_client.db
                lusers = list(db.users.find({"email":auth.username}))


                if auth.username == lusers[0]['email'] and password == lusers[0]['password'] and len(lusers) > 0:
                    token = JwtSystem.create_token(auth.username)
                    return jsonify({
                        'token': token,
                        'name': lusers[0]['name'],
                        'email': lusers[0]['email'],
                        'dev': lusers[0]['dev'],
                        'avatar': lusers[0]['avatar']
                    })
                
                return Response(json.dumps({'code': 1, 'status': False}), status=401, mimetype='application/json')

            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')

        ###
        # POST - /token-verify
        ###
        @app.route('/token-verify', methods=['POST'])
        @JwtSystem.token_required
        def token_verify():
            try:
                return Response(json.dumps({ "code": 0, "authorization": True}), status=200, mimetype='application/json')

            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')
