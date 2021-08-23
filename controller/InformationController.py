import json
from flask import request, Response, jsonify
from flask_cors import CORS

class InformationController:

    def __init__(self, app):

        @app.route('/api-information', methods=['GET'])
        def ApiInformation():
            try:
                resp = json.dumps({
                    "code": 0,
                    "dev": 'Willian Takashi Ishida',
                    "version": '1.0.0'
                })
                return Response(resp, status=200, mimetype='application/json')
            except Exception as e:
                resp = json.dumps({"error": str(e)})
                return Response(resp, status=400, mimetype='application/json')