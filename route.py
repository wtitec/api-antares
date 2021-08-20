from controller.InformationController import InformationController
from controller.TestesController import TestesController
import controller


class Route:

    def __init__(self, app):
        TestesController(app)
        InformationController(app)
