from flask import request, abort
from flask_restful import Resource, reqparse
from math import radians, cos, sin, asin, sqrt

from app import db, Restaurant, restaurant_schema, restaurants_schema

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371000 # Radius of earth in meters.
    return c * r


class Statistics(Resource):
    def get(self):
        lat = float(request.args['latitude'])
        lng = float(request.args['longitude'])
        rad = float(request.args['radius'])
        restaurants_within = []
        ratings = []
        restaurants = Restaurant.query.all()
        all_restaurants = restaurants_schema.dump(restaurants)
        for res in all_restaurants:
            distance = haversine(lng,lat,res['lng'],res['lat']) 
            if distance <= rad:
                restaurants_within.append(res)
                ratings.append(res['rating'])
                # print(distance)
        if ratings:
            count = len(ratings)
            avg = sum(ratings)/count
            std = sqrt(sum((x-avg)**2 for x in ratings) / count)
        else:
            abort(404, "No restaurants found")
        return {"count" : count, "avg" : avg, "std" : std}, 200

    