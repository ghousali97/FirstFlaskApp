from werkzeug.security import safe_str_cmp #installed with Flask-JWT, slloes us to safely compare strings as it handles encoding
from models.user import UserModel


def authenticate(username,password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password):
        return user
def identity(payload): #payload is content of  JWT token
    user_id = payload['identity'] #we extract user ID from the content
    return User.find_by_id(user_id)
