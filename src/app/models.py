from . import db
from sqlalchemy import Column, String, DateTime
from datetime import datetime


class email(db.Model):

    __tablename__ = "emails"

    email = db.Coloumn(db.String(250), primary_key=True)
    first_name = db.Coloumn(db.String(250), nullable=False)
    last_name = db.Coloumn(db.String(250), nullable=False)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)

