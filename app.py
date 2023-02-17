import json

from flask import Flask, request
from flask_migrate import Migrate

from config import SQLALCHEMY_DATABASE_URI, API_PATH
from db_models import db
import db_steps


def handle_request(path):
    try:
        request_body = request.get_json() if request.data else {}
        query_string = request.query_string
        if query_string:
            path += f'?{query_string.decode("utf-8")}'
        db_steps.add_request(path, request_body)
        return db_steps.get_re_entry_by_string(path, request_body), 200
    except IndexError:
        return 'There is no such pattern in DB', 400


def create_app():
    app_ = Flask(__name__)
    app_.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app_)
    with app_.app_context():
        db.create_all()
    return app_


app = create_app()
migrate = Migrate(app, db)


@app.route(f'/{API_PATH}', methods=['GET', 'POST', 'PUT'])
@app.route(f'/{API_PATH}/<path:path>', methods=['GET', 'POST', 'PUT'])
def catch_all_api(path):
    return handle_request(path)


@app.route('/add_pattern', methods=['POST'])
def add_pattern():
    result = request.get_json()
    db_steps.add_entry(result.get('path'), result.get('payload'), result.get('request_body_pattern'))
    return '', 204


@app.route('/clean_db', methods=['GET'])
def clean_db():
    db_steps.clean_db()
    return 'DB was cleaned', 200


@app.route('/get_all_mocks', methods=['GET'])
def get_all_mocks():
    return str(db_steps.get_all_entries()), 200


@app.route('/requests_history', methods=['GET'])
def get_requests_history():
    return json.dumps([{'id': x.id, 'path': x.path, 'body': x.body} for x in db_steps.get_all_requests()]), 200


if __name__ == '__main__':
    app.run(debug=True)
