import sqlite3
from flask_restful import Resource
from flask_restful import reqparse

class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() #responsible for executing the queries and getting results
        query ="SELECT * FROM users WHERE username=?"
        result = cursor.execute(query,(username,)) #the second argument needs to be a tuple always so follow this syntax for single values
        row = result.fetchone() #returns the first row / result
        if row:
            user = cls(*row)# this means cls(row[0],row[1],row[2]) cls means current classs
        else:
            user = None
        connection.close()

        return user

    @classmethod
    def find_by_id(cls,_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() #responsible for executing the queries and getting results
        query ="SELECT * FROM users WHERE id=?"
        result = cursor.execute(query,(_id,)) #the second argument needs to be a tuple always so follow this syntax for single values
        row = result.fetchone() #returns the first row / result
        if row:
            user = cls(*row)# this means cls(row[0],row[1],row[2]) cls means current classs
        else:
            user = None
        connection.close()

        return user

class UserRegister(Resource):
    def post(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor() #
        query = "INSERT INTO users VALUES(null, ?,?)" #IGNORE to supress duplication error

        parser = reqparse.RequestParser() #initialises the parse object
        parser.add_argument("username",
        type=str,
        required=True,
        help="Username can't be blank")

        parser.add_argument("password",
        type=str,
        required=True,
        help="password can't be blank")

        data = parser.parse_args() #parses incoming request, will ignore all argument not explicitly "added"

        if User.find_by_username(data['username']):
            connection.commit()
            connection.close()
            return {"message":"User {} already exists".format(data['username'])}, 400
        else:
            result = cursor.execute(query,(data['username'],data['password']))
            connection.commit()
            connection.close()
            return {"message":"User {} registered successfully".format(data['username'])}, 201
