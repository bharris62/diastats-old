from flask_restful import Resource, reqparse
from flask import jsonify
from models.user import UserModel

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    parser.add_argument('first_name',
        type=str,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('last_name',
        type=str,
        required=False,
        help="This field cannot be blank."
    )
    parser.add_argument('birth_year',
        type=int,
        required=True,
        help="This field cannot be blank."
    )

    def post(self):
        data = User.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists. Username and Email must be unique"}, 400
        elif UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists. Username and Email must be unique"}, 400

        user = UserModel(data['email'], data['username'], data['password'], data['first_name'], data['last_name'], data['birth_year'])

        user.save_to_db()

        return user.json()