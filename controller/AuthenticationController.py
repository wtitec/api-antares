from itertools import filterfalse
import json
from flask import request, Response
from flask.json import jsonify
from system.jwt.JwtSystem import JwtSystem



class AuthenticationController:

    def __init__(self, app):
        ###
        # POST - /login
        ###
        @app.route('/login', methods=['POST'])
        def token():
            try:
                auth = request.authorization

                if auth.username == 'wti.designer@gmail.com' and auth.password == '1qaz':
                    token = JwtSystem.create_token(auth.username)
                    return jsonify({'token': token})
                
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
