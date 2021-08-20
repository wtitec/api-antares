import json
from flask import request, Response
from flask.json import jsonify
from system.jwt.JwtSystem import JwtSystem



class TestesController:

    def __init__(self, app):
        ###
        # POST - /login
        ###
        @app.route('/login', methods=['POST'])
        def token():
            try:
                auth = request.authorization

                if auth.username == 'test' and auth.password == 'test':
                    token = JwtSystem.create_token(auth.username)
                    return jsonify({'token': token})
                return Response({}, status=200, mimetype='application/json')

            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')

        ###
        # POST - /json
        ###
        @app.route('/json', methods=['POST'])
        @JwtSystem.token_required
        def index():
            
            try:
                content = request.get_json()
                resp = json.dumps({
                    "teste": content['id'],
                    "status": 0
                })
                return Response(resp, status=200, mimetype='application/json')
            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')

        ###
        # GET - /version
        ###
        @app.route('/version', methods=['GET'])
        def version():
            try:
                resp = json.dumps({
                    "version": "0.0.0"
                })
                return Response(resp, status=200, mimetype='application/json')
            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')
