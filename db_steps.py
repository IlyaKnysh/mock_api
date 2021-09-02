import re

import app
from db_models import Payload, db


def add_entry(path_pattern, payload):
    with app.app.app_context():
        payload = Payload(path_pattern=path_pattern, payload=payload)
        db.session.add(payload)
        db.session.commit()


def get_add_entries():
    with app.app.app_context():
        return Payload.query.all()


def kill_db():
    with app.app.app_context():
        db.drop_all()


def get_re_entry_by_string(path):
    with app.app.app_context():
        all_data = Payload.query.all()
        return list(filter(lambda x: re.match(x.path_pattern, path), all_data))[0].payload


def clean_db():
    with app.app.app_context():
        db.drop_all()
        db.create_all()
