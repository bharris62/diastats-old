from db import db
from datetime import datetime

class BolusModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=lambda x: datetime.utcnow())
    time_submitted = db.Column(db.DateTime, default=datetime.utcnow())
    bolus = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date, bolus, user_id):
        self.date = date
        self.bolus = bolus
        self.user_id = user_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()