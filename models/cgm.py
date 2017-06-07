from db import db
from datetime import datetime

class CGM(db.Model):
    __tablename__ = 'cgm'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=lambda x: datetime.utcnow())
    time_submitted = db.Column(db.DateTime, default=datetime.utcnow())
    bg = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, date, bg, user):
        self.date = date
        self.bg = bg
        self.user_id = user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()