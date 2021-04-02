from werkzeug.security import safe_str_cmp #installed with Flask-JWT, slloes us to safely compare strings as it handles encoding
from user import User

users = [
User(1,'bob','1234')

]

username_mapping = {u.username:u for u in users}

userid_mapping = {u.id:u for u in users}

def authenticate(username,password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user
def identity(payload): #payload is content of  JWT token
    user_id = payload['identity'] #we extract user ID from the content
    return User.find_by_id(user_id)
