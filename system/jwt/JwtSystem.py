from flask import request, jsonify
import jwt
import datetime
from functools import wraps

SECRET_KEY = "118972de9c42c227d41bf8b6a8c0a31b74418b24951b1e7c8c8ca09ccd1c1301"

class JwtSystem:
   
    def token_required(f):
        @wraps(f)
        def decorator(*args, **kwargs):

            token = None

            if 'Authorization' in request.headers:
                token = request.headers['Authorization'].replace(
                    'Bearer ', '')

            if not token:
                return jsonify({'message': 'a valid token is missing'}),400

            try:
                data = jwt.decode(
                    token, SECRET_KEY, algorithms=["HS256"])
            except:
                return jsonify({'message': 'token is invalid', 'data': request.headers }),401

            return f(*args, **kwargs)
        return decorator

    def create_token(username):
        time_expire = 60*60*24
        return jwt.encode({'user': username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=time_expire)}, SECRET_KEY, algorithm="HS256")