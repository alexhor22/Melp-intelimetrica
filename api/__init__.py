from flask_restful import Api

from app import app
from .Restaurants import Restaurants

restServer = Api(app)

restServer.add_resource(Restaurants,"/restaurants")