import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class User_register(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )




    def post(self):

        data = User_register.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "Username already exist"}


        user=UserModel(data['username'],data['password'])
        user.save_to_db()

        

        return {"message":"User created succesfully"}
