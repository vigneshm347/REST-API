import sqlite3 as db
from flask_restful import Resource, reqparse
from models.user import UserModel
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be empty"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be empty"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']) is None:
            user = UserModel(**data)
            user.save_to_db()

        else:
            return {"message": "User exist"}, 400

        return {"message": "user Created"}, 201