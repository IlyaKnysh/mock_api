from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()
meta = MetaData()


class Payload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path_pattern = db.Column(db.String(255), unique=True, nullable=False)
    payload = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Pattern: {self.path_pattern}\nPayload: {self.payload}\n\n'
