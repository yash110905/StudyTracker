from database import db
from flask_login import UserMixin

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) 

    email = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )#Required & unique email

    password = db.Column(
        db.String(200),
        nullable=False
    )#Required password
    #email
    def __repr__(self):
        return self.email