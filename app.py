import os
import csv
import math
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from sqlalchemy.ext.hybrid import hybrid_method

app = Flask(__name__) 
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Restaurant(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    rating = db.Column(db.Integer)
    name = db.Column(db.String(50))
    site = db.Column(db.String(50))
    email = db.Column(db.String(50))
    phone = db.Column(db.String(15))
    street = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(25))
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)

    def __init__(self, id, rating, name, site, email, phone, street, city, state, lat, lng):
        self.id = id
        self.rating = rating
        self.name = name
        self.site = site
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.lat = lat
        self.lng = lng

class RestaurantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng')

restaurant_schema = RestaurantSchema()
restaurants_schema = RestaurantSchema(many=True)

def create_db():
    db.drop_all()
    db.create_all()
    with open('restaurantes.csv',encoding='utf-8') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in data:
            if count > 0:
                id = row[0]
                rating = int(row[1])
                name = row[2]
                site = row[3]
                email = row[4]
                phone = row[5]
                street = row[6]
                city = row[7]
                state = row[8]
                lat = float(row[9])
                lng = float(row[10])
                
                new_restaurant = Restaurant(id, rating, name, site, email, phone, street, city, state, lat, lng)
                db.session.add(new_restaurant)
                db.session.commit()

            count = count + 1

@app.route('/restaurants/all', methods=['GET'])
def get_restaurants():
    all_restaurants = Restaurant.query.all()
    result = restaurants_schema.dump(all_restaurants)
    print(len(result))
    return jsonify(result)

if __name__ == '__main__':
    from api import *
    create_db()
    app.run(host='0.0.0.0',debug=True)