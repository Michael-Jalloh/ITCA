from flask_restful import Resource, reqparse
import logging
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('first_name')
parser.add_argument('last_name')



class Signup(Resource):
    decorators = []

    def post(self):
        logger = logging.getLogger('app.user-signup-post')
        data = parser.parse_args()
        user = User()
        user.username = data['username']
        user.email = data['email']
        user.password = data['password']
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        try:
            user.save()
            user.generate_keys()
            return {
                'data':user.details(),
                'message':'Your account has been created',
                'status':'succes'
                }
        except Exception as e:
            logger.error(str(e))
            return {
                'data':'',
                'message':'An error occur',
                'status':str(e)
                }

class Verify(Resource):
    def post(self):
        data = parser.parse_args()
        logger = logging.getLogger('app.user-login-post')
        try:
            email = data['email']
            password = data['password']
            user = User.get(User.email == email)
            if user is not None and user.verify_password(password):
                return {
                    'status':'success',
                    'message':'user verified',
                    'data':  user.details()
                    }
            else:
                return {
                        'status':'error',
                        'message':'Wrong credentials'
                        }

        except Exception as e:
            logger.error(str(e))
            return {
                    'status':'error',
                    'message':str(e)
                    }
