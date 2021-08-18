from flask import Flask
from route import Route

application = Flask(__name__)
Route(application)
if __name__ == '__main__':
    application.run()