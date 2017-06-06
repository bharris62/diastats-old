from flask_restful import Resource, reqparse
from flask import jsonify
from models.user import UserModel
from datetime import datetime
from models.meter import MeterModel
from services.livongo import ScrapeLivongo


class Meter(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('bg',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="This field cannot be blank."
                        )


    def post(self):
        data = Meter.parser.parse_args()
        user = UserModel.find_by_id(data['user_id'])
        d = data['date'].split('/')
        date = datetime(int(d[0]), int(d[1]), int(d[2]))
        meter = MeterModel(date, data['bg'], user.id)

        meter.save_to_db()


class MeterScrape(Resource):

    def post(self, id):
        ScrapeLivongo.scrape(id)
