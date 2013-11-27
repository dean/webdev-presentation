from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from demo import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, username, name, password):
        self.username = username
        self.name = name
        self.password = password
