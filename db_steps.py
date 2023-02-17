import json
import re

import app
from db_models import Payload, db, Request
from logger import LOGGER


def add_entry(path_pattern, payload, request_body=None):
    with app.app.app_context():
        payload = Payload(path_pattern=path_pattern, payload=str(payload), request_body_pattern=request_body)
        db.session.add(payload)
        db.session.commit()


def get_all_entries():
    with app.app.app_context():
        return Payload.query.all()


def kill_db():
    with app.app.app_context():
        db.drop_all()


def get_re_entry_by_string(path, request_body):
    with app.app.app_context():
        all_data = Payload.query.all()
        filter_payload = list(filter(lambda x: re.match(x.path_pattern, path), all_data))
        if request_body:
            filter_by_body_payload = list(
                filter(lambda x: re.match(x.request_body_pattern, json.dumps(request_body)), filter_payload))
        payload_to_return = filter_by_body_payload[0].payload if request_body else filter_payload[0].payload
        LOGGER.info(f'RESPONSE: {payload_to_return}')
        return payload_to_return


def add_request(path, body=None):
    with app.app.app_context():
        req = Request(path=path, body=json.dumps(body))
        db.session.add(req)
        db.session.commit()


def clean_db():
    with app.app.app_context():
        db.drop_all()
        db.create_all()


def get_all_requests():
    with app.app.app_context():
        return Request.query.all()


if __name__ == '__main__':
    print(get_all_entries())
