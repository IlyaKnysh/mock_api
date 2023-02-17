from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()
meta = MetaData()


class Payload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path_pattern = db.Column(db.String(255), nullable=False)
    payload = db.Column(db.String(), nullable=False)
    request_body_pattern = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'path_pattern: {self.path_pattern}\npayload: {self.payload}\nrequest_body: {self.request_body_pattern}\n\n'


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(), nullable=True)

    def __repr__(self):
        return f'path: {self.path}\nbody: {self.body}\n\n'
