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

                if len(lusers) > 0:
                    if auth.username == lusers[0]['email'] and password == lusers[0]['password']:
                        token = JwtSystem.create_token(auth.username)
                        if 'avatar' in lusers[0]:
                            avatar = lusers[0]['avatar']
                        else:
                            avatar = "https://lh3.googleusercontent.com/proxy/Mcr4Cry35DGvL10b13kzEGoHuiXeCIBstVDk_gmafShjvOYdvZ8K3_yX6Lbh17szb_42UQg6mG_J1wouVx5JTfxUohIQl1wUQbsAx3GDV-TFLni38Ig"
                        
                        return jsonify({
                            'token': token,
                            'name': lusers[0]['name'],
                            'email': lusers[0]['email'],
                            'dev': lusers[0]['dev'],
                            'avatar': avatar
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
