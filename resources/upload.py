import werkzeug
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import datetime
from models.pump import BolusModel
from models.cgm import CGM
import pandas as pd


class UploadTandem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

    def post(self, id):
        data = UploadTandem.parser.parse_args()

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


class UploadDexcom(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

    def post(self, id):
        data = UploadDexcom.parser.parse_args()
        logger = 0
        for d in data['file']:
            d = d.decode('utf-8').split(",")

            if str(d[1]).startswith('20'):

                date = datetime.datetime.strptime(d[1].replace("T", " "), "%Y-%m-%d %H:%M:%S")
                bg = float(d[7])
                dat = CGM(date, bg, id)
                dat.save_to_db()
                logger += 1

        print("logged {} items".format(logger))
