from car import Car, Cars
import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        find = "SELECT * FROM users WHERE username = ?"
        result = cur.execute(find, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        conn.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        find = "SELECT * FROM users WHERE id = ?"
        result = cur.execute(find, (_id,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        conn.close()
        return user
    
def authenticate(username, password):
        user = User.find_by_username(username)
        if user and password == user.password:
            return user
def identity(payload):
        user_id = payload['identity']
        return User.find_by_id(user_id)
                
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help='Please provide a valid username')
    parser.add_argument("password", type=str, required=True, help='Please provide a valid password')
    def post(self):
        try:
            data = UserRegister.parser.parse_args()

            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE username=?"
            result = cursor.execute(query, (data['username'],))
            row = result.fetchone()
            if row:
                return {"message": "This user already exists"}
            query = "INSERT INTO users VALUES (null, ?, ?)"
            cursor.execute(query, (data['username'], data['password']))
            conn.commit()
            conn.close()
            return {"message": "User created successfully"}, 201
        except:
            return {
                "message": "Internal Server Error"
                }, 500
        
