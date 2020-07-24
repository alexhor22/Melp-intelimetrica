# Melp-intelimetrica
This API implemets CRUD operations for a Restaurant database. It also implements a statistical analysis of the restaurants within the database.

The API is developed in **Python3** using **Flask** as the main framework. The database is managed with **SQLite** and uses **SQLAlchemy** as an ORM.  

This API is deployed at <br/>
    https://melp-intelimetrica-restaurants.herokuapp.com/

This are the dependencies requirements for running locally the API, which can also be found in the file *requirements.txt*

```
Click==7.0
Flask==1.1.2
flask-marshmallow==0.13.0
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.4
gunicorn==20.0.4
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
marshmallow==3.7.1
marshmallow-sqlalchemy==0.23.1
requests==2.23.0
simplejson==3.17.0
SQLAlchemy==1.3.18
urllib3==1.25.8
Werkzeug==1.0.1 
```
*Melp-intelimetrica.postman_collection.json* is an exported **Postman** collection, which can be imported to test request to the deployed API.

# Endpoints:

## URL :
## *https://melp-intelimetrica-restaurants.herokuapp.com/restaurants*
#### GET :

#### Description
Returns a restaurant given an Id
#### Parameters
*Header Parameters* <br/>

    id : [string]
#### Response
    {
    "site": [string],
    "state": [string],
    "lng": [float],
    "city": [string],
    "id": [string],
    "email": [string],
    "rating": [int],
    "name": [string],
    "street": [string],
    "lat": [float],
    "phone": [string]
    }

<br/>

#### PUT :

#### Description
Modifies any attribute of a restaurant given by its Id. Returns the modified restaurant.
#### Parameters
*Header Parameters* <br/>

    id : [string]
Any of these:<br/>

    site : [string]
    state : [string]
    lng : [float]
    city : [string]
    email : [string]
    rating : [int]
    name : [string]
    street : [string]
    lat : [float]
    phone : [string]
#### Response
    {
    "site": [string],
    "state": [string],
    "lng": [float],
    "city": [string],
    "id": [string],
    "email": [string],
    "rating": [int],
    "name": [string],
    "street": [string],
    "lat": [float],
    "phone": [string]
    }

<br/>

#### POST :

#### Description
Adds a new restaurant to the database. Returns the added restaurant.
#### Parameters
*Request body parameters* <br/>

    {
    "site": [string],
    "state": [string],
    "lng": [float],
    "city": [string],
    "id": [string],
    "email": [string],
    "rating": [int],
    "name": [string],
    "street": [string],
    "lat": [float],
    "phone": [string]
    }
#### Response
    {
    "site": [string],
    "state": [string],
    "lng": [float],
    "city": [string],
    "id": [string],
    "email": [string],
    "rating": [int],
    "name": [string],
    "street": [string],
    "lat": [float],
    "phone": [string]
    }

<br/>

#### DEL :

#### Description
Deletes a restaurant given an Id. Returns the deleted restaurant.
#### Parameters
*Header Parameters* <br/>

    id : [string]
#### Response
    {
    "site": [string],
    "state": [string],
    "lng": [float],
    "city": [string],
    "id": [string],
    "email": [string],
    "rating": [int],
    "name": [string],
    "street": [string],
    "lat": [float],
    "phone": [string]
    }

<br/>

---
## URL : 
## *https://melp-intelimetrica-restaurants.herokuapp.com/restaurants/statistics*
#### GET :

#### Description
Calculates the ratings average and standard deviation of restaurants within a radius given a latitude, longitude and radius in meters. Returns the calculations and quantity of restaurants within the area.
#### Parameters
*Header Parameters* <br/>

    latitude : [float]
    longitude : [float]
    radius : [float]
#### Response
    {
    "count" : [integer],
    "avg" : [float],
    "std" : [float]
    }