from flask import Flask
from route import Route
from flask_cors import CORS

application = Flask(__name__)
application.config["MONGO_URI"] = "mongodb://aldebaran:accenturechallange_1qazxsw2@18.228.225.100:27017/accenture_challenge?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false"
CORS(application)

Route(application)
if __name__ == '__main__':
    application.run()