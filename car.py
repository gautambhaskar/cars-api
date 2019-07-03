import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Car(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help="Please enter a valid model name" )
    parser.add_argument('make', type=str, required=True, help="Please enter a valid manufacturer name" )
    parser.add_argument('power', type=str, required=True, help="Please enter a valid bhp number" )
    def ispresent(name_arg):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM cars WHERE name=?'
        result = cursor.execute(query, (name_arg.upper(),))
        row = result.fetchone()
        if row:
            return True
        return False
    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM cars WHERE name=?'
        result = cursor.execute(query, (name.upper(),))
        row = result.fetchone()
        if row:
            car = {
                "name": row[0],
                "make": row[1],
                "power": row[2]
            }
        else:
            car = None
            return {"message": "Car Not Found in DB"}, 404
        return car 
    @jwt_required()  
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM cars WHERE name=?'
        result = cursor.execute(query, (name.upper(),))
        row = result.fetchone()
        if row:
            car = {
                "name": row[0],
                "make": row[1],
                "power": int(row[3])
            }
            delete = "DELETE FROM cars WHERE name=?"
            cursor.execute(delete, (name.upper(),))
            connection.commit()
            connection.close()
            return {
                "message": "Deleted Successfully",
                "original": car
            }
        connection.close()
        return {"message": "Car Not Found in DB"}, 404

    @jwt_required()
    def put(self, name):
        cars = []
        data = Car.parser.parse_args()
        data['name'] = data['name'].replace(" ", "_")
        if Car.ispresent(data['name'].upper()) and name.upper() != data['name'].upper():
            return {
                "message": "Car with given Name is already in DB"
            }
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = 'SELECT * FROM cars WHERE name=?'
        result = cursor.execute(query, (name.upper(),))
        row = result.fetchone()
 
        if row:
            car = {
                "name": row[0],
                "make": row[1],
                "power": row[2]
            }
            query2 = "DELETE FROM cars WHERE name = ?"
            cursor.execute(query2, (name.upper(),))
            query3 = "INSERT INTO cars VALUES( ?, ?, ?)"
            cursor.execute(query3, (data['name'], data['make'], int(data['power'])))
        else:
            car = None
            return {"message": "Car Not Found in DB"}, 404
        connection.commit()
        result = cursor.execute("SELECT * FROM cars")
        for row in result:
            cars.append({
                "name" : row[0],
                "make": row[1],
                "power":  int(row[2])
            })
        connection.close()
        return {"message": "Success! Car was edited on DB",
        "cars": cars,
        "original": car}, 200
class Cars(Resource):
    @jwt_required()
    def post(self):
        data = Car.parser.parse_args()
        data['name'] = data['name'].replace(" ", "_")
        if Car.ispresent(data['name']):
            return {
                "message": "Car with given Name is already in DB"
            }
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        check = "SELECT * FROM cars WHERE name=?"
        rows = cursor.execute(check, (data['name'].upper().replace(" ", "_"),))
        row = rows.fetchone()
        if row:
            return {"message": "This car is already in the DB"}, 400
            conn.close()
        else:
            query = "INSERT INTO cars VALUES( ?, ?, ?)"
            cursor.execute(query, (data['name'].upper().replace(" ", "_"), data['make'].upper().replace(" ", "_"), int(data['power'])))
            conn.commit()
            conn.close()
            return {"message": "Car added to DB"}, 201
    @jwt_required()
    def get(self):
        cars = []
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        result = cursor.execute("SELECT * FROM cars")
        for row in result:
            cars.append({
                "name" : row[0],
                "make": row[1],
                "power":  int(row[2])
            })
        return {"cars": cars}
