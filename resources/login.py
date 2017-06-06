from flask_restful import Resource, reqparse
from models.user import UserModel
from models.login import LoginModel

class ScrapeLogin(Resource):

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('website',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )

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

        parser.add_argument('user_id',
                            type=str,
                            required=True,
                            help="This field cannot be blank."
                            )
        data = ScrapeLogin.parser.parse_args()
        user = UserModel.find_by_id(data['user_id'])

        login = LoginModel(data['website'], data['username'], data['password'], user.id)

        login.save_to_db()

    def get(self):

        info = LoginModel.find_by_id(1)
        print(info)




