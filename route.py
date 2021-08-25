from controller.AuthenticationController import AuthenticationController
from controller.UserController import UserController
from controller.InformationController import InformationController
from controller.TestesController import TestesController
import controller


class Route:

    def __init__(self, app):
        AuthenticationController(app)
        UserController(app)
        TestesController(app)
        InformationController(app)
