from flask import Flask
from route import Route
from flask_cors import CORS

application = Flask(__name__)

CORS(application)

Route(application)
if __name__ == '__main__':
    application.run()