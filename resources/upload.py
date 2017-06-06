import werkzeug
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
import pandas as pd
import xlrd
import csv

class Upload(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files')

    def post(self):
        data = Upload.parser.parse_args()
        print(data['file'])
        read = pd.read_csv(data['file'], skiprows=range(6))
        print(read)
