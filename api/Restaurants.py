from flask import request, abort
from flask_restful import Resource, reqparse

from app import db, Restaurant, restaurant_schema, restaurants_schema

class Restaurants(Resource):
    def get(self):
        id = request.args['id']
        restaurant = Restaurant.query.get(id)
        return restaurant_schema.dump(restaurant), 200

    def post(self):
        params = request.get_json()
        errors = restaurant_schema.validate(params)
        if errors:
            abort(400, str(errors))

        new_restaurant = Restaurant(params['id'], params['rating'],
                                    params['name'], params['site'],
                                    params['email'], params['phone'],
                                    params['street'], params['city'],
                                    params['state'], params['lat'], params['lng'])
        
        db.session.add(new_restaurant)
        db.session.commit()
        return restaurant_schema.dump(new_restaurant) ,200

    def put(self):
        params = request.args
        id = params['id']
        restaurant = Restaurant.query.get(id)

        restaurant.rating = params['rating'] if 'rating' in params else restaurant.rating
        restaurant.name = params['name'] if 'name' in params else restaurant.name
        restaurant.site = params['site'] if 'site' in params else restaurant.site
        restaurant.email = params['email'] if 'email' in params else restaurant.email
        restaurant.phone = params['phone'] if 'phone' in params else restaurant.phone
        restaurant.street = params['street'] if 'street' in params else restaurant.street
        restaurant.city = params['city'] if 'city' in params else restaurant.city
        restaurant.state = params['state'] if 'state' in params else restaurant.state
        restaurant.lat = params['lat'] if 'lat' in params else restaurant.lat
        restaurant.lng = params['lng'] if 'lng' in params else restaurant.lng
        
        db.session.commit()

        return restaurant_schema.dump(restaurant), 200

    def delete(self):
        id = request.args['id']
        restaurant = Restaurant.query.get(id)
        db.session.delete(restaurant)
        db.session.commit()
        
        return restaurant_schema.dump(restaurant), 200