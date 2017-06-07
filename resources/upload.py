import werkzeug
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import datetime
from models.pump import BolusModel
import pandas as pd
import xlrd
import csv

class Upload(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

    def post(self, id):
        data = Upload.parser.parse_args()

        iter = 0
        for d in data['file']:
            d = d.decode('utf-8').replace('\r\n', "")
            d = d.split(",")
            try:
                # Get IOB values
                # iob, some code, date, bolus amt
                if d[0].replace('"', "") == 'IOB':
                    iob = d[0].replace('"', "")
                    code = d[1].replace('"', "")
                    date = datetime.datetime.strptime(d[2].replace('"', "").replace("T", " "), "%Y-%m-%d %H:%M:%S")
                    bolus = d[3].replace('"', "")
                    data = BolusModel(date, float(bolus), id)
                    data.save_to_db()
                    print(iob, code, date, bolus)
            except BaseException as e:
                print(e)

            iter += 1
            # if iter==20:
            #     break