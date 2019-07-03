import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Driver(Resource):
    def find_by_name(name):
        query = "SELECT * FROM drivers WHERE name=?"
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        return row
    parser = reqparse.RequestParser()
    parser.add_argument('driver', type=str, required=True, help="Please submit a valid driver name")
    parser.add_argument('team', type=str, required=True, help="Please submit a valid team name")
    parser.add_argument('rating', type=float, required=True, help="Please submit a valid driver rating (0-5)")
    @jwt_required()
    def get(self, driver):
        row = Driver.find_by_name(driver.upper())
        if row:
            found_driver = {
                "driver": row[0],
                "team": row[1],
                "rating": row[2]
            }
            return { 
                "message": "Driver retrieved successfully",
                "driver": found_driver 
            }
        else:
            return {
                "message": "Driver Not Found"
            }, 404
    @jwt_required()
    def put(self, driver):
        data = Driver.parser.parse_args()
        if float(data['rating']) > 5 or float(data['rating']) < 0:
            return {
                "message": "Please submit a valid driver rating (0-5)"
            }
        row_check = Driver.find_by_name(data['driver'].upper().replace(" ","_"))
        if row_check:
            return {
                "message": "A driver with the given name already exists in the DB"
            }, 400
        row = Driver.find_by_name(driver.upper())
        if row:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            delete_query = "DELETE FROM drivers WHERE name=?"
            # cursor.execute(delete_query, (driver.upper(),))
            update_query = "UPDATE drivers SET name=?, team=?, rating=? WHERE name=?"
            cursor.execute(update_query, (data['driver'].upper().replace(" ","_"), data['team'].upper().replace(" ","_"), float(data['rating']), driver.upper()))
            connection.commit()
            connection.close()
            return {
                "message": "Driver updated successfully"
            }, 200
        else:
            return {
                "message": "Driver Not Found"
            }, 404
    @jwt_required()
    def delete(self, driver):
        row = Driver.find_by_name(driver.upper().replace(" ","_"))
        if row:
            delete = "DELETE FROM drivers WHERE name=?"
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            cursor.execute(delete, (driver.upper().replace(" ","_"),))
            connection.commit()
            connection.close()
            return {
                "message": "Deleted successfully"
            }, 200
        else:
            return {
                "message": "Driver Not Found"
            }, 404
class Drivers(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('driver', type=str, required=True, help="Please submit a valid driver name")
    parser.add_argument('team', type=str, required=True, help="Please submit a valid team name")
    parser.add_argument('rating', type=float, required=True, help="Please submit a valid driver rating (0-5)")
    def find_by_name(name):
        query = "SELECT * FROM drivers WHERE name=?"
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        return row
    @jwt_required()
    def post(self):
        data = Driver.parser.parse_args()

        if float(data['rating']) > 5 or float(data['rating']) < 0:
            return {
                "message": "Please submit a valid driver rating (0-5)"
            }

        data['driver'] = data['driver'].upper().replace(" ","_")
        data['team'] = data['team'].upper().replace(" ","_")
        row = Drivers.find_by_name(data['driver'])
        if row:
            return {
                "message": "A driver with the given name already exists in the DB"
            }, 400
        new_driver = (data['driver'], data['team'], data['rating'])
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        post_query = "INSERT INTO drivers VALUES(?,?,?)"
        cursor.execute(post_query, new_driver)
        connection.commit()
        connection.close()
        return {
            "message": "Driver successfully added to DB"
        }, 201
    @jwt_required()
    def get(self):
        try:
            query = "SELECT * FROM drivers"
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()
            drivers = []
            result = cursor.execute(query)
            for row in result:
                drivers.append({
                    "driver": row[0],
                    "team": row[1],
                    "rating": row[2]
                })
            return {
                "message": "Drivers retrieved successfully",
                "drivers": drivers
            }, 200
        except:
            return {
                "message": "Internal Server Error"
            }, 500
        
        
