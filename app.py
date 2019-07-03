from flask import Flask
from flask_restful import Resource, Api, reqparse
import sqlite3
from car import Car, Cars
from auth import authenticate, identity, UserRegister
from flask_jwt import JWT, jwt_required
from driver import Driver, Drivers
app = Flask(__name__)
app.secret_key = '440579'
api = Api(app)

jwt = JWT(app, authenticate, identity)


api.add_resource(Car, '/cars/<string:name>')
api.add_resource(Cars, '/cars')
api.add_resource(UserRegister, '/register')
api.add_resource(Driver, '/drivers/<string:driver>')
api.add_resource(Drivers, '/drivers')
if __name__ == '__main__':
    app.run(port=5000, debug=True)

#NEXT TASKS: 
#ADD /<NAME:STRING>/<DRIVER:STRING> CAPABILITIES
#ALLOW FOR LIST OF DRIVERS BASED ON ROOT:
# /<NAME:STRING>
# FROM THERE YOU CAN GET LIST OF ALL DRIVERS AND...
# ADD INDIVIDUAL DRIVERS
# USE THE MORE DETAILED URL TO ACCESS EACH DRIVER AND ALLOW FOR GET PUT & DELETE

