from db import db
from datetime import datetime

class LoginModel(db.Model):
    __tablename__ = 'logins'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    site = db.Column(db.String(255), nullable=False)
    time_submitted = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __init__(self, site, username, password, user_id):
        self.site = site
        self.username = username
        self.password = password
        self.user_id = user_id

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

