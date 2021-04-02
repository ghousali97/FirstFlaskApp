from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity #these are the functions we created
from resources.user import UserRegister
from resources.item import Item, ItemList

app =Flask(__name__)
app.secret_key = "key" #secret key that needs to be protected in future
jwt = JWT(app, authenticate, identity) #create /auth endpoint
                                    #when we call /auth we send it username and password which is passed to authenticate function
                                    #once authenticated JWT returns a JWT token in response to /authenticate
                                    #on subsequent requests JWT token is passed to identy which returns a user object.
                                    #auth request should have content-type JSON

api = Api(app) #Api works with resourcs and every resource has to be a class.




api.add_resource(Item, '/item/<string:name>') #binds the resource to a URL
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5002, debug=True)
