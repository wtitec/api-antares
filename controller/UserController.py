from itertools import filterfalse
import json
from flask import request, Response
from flask.json import jsonify
from system.jwt.JwtSystem import JwtSystem
from flask_pymongo import PyMongo
import hashlib

class UserController:

    def __init__(self, app):

        ###
        # POST - /adduser
        ###
        @app.route('/adduser', methods=['POST'])
        def adduser():
            
            try:
                content = request.get_json()

                password = hashlib.sha256(content['password'].encode('utf-8')).hexdigest()
                
                try:
                    mongodb_client = PyMongo(app)
                    db = mongodb_client.db
                    db.users.insert_one({
                        "name": content['name'],
                        "email": content['email'],
                        "dev": content['dev'],
                        "password": password
                    })
                except Exception as e:
                    resp = json.dumps({"error": str(e)})
                    return Response(resp, status=400, mimetype='application/json')

                resp = json.dumps({
                    "code": 0,
                    "msg" : "Success!"
                })

                return Response(resp, status=200, mimetype='application/json')
            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')