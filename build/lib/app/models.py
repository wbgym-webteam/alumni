from . import db


class email(db.Model):

    __tablename__ = "emails"

    email = db.Coloumn(db.String(250), primary_key=True)
    time_stamp = db.Coloumn(db.DateTime, Default=datetime.utcnow)

