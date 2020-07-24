from flask_restful import Api

from app import app
from .Restaurants import Restaurants
from .Statistics import Statistics

restServer = Api(app)

restServer.add_resource(Restaurants,"/restaurants")
restServer.add_resource(Statistics,"/restaurants/statistics")