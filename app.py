from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_bcrypt import Bcrypt
from models import meter, user
from security import authenticate, identity
from resources.user import User
from resources.meter import Meter

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/diastats'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.secret_key = 'Super secret key'

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(User, '/register')
api.add_resource(Meter, '/v1/meter')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run()
