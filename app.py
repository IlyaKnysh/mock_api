from flask import Flask, request
from flask_migrate import Migrate

from config import SQLALCHEMY_DATABASE_URI
from db_models import db
import db_steps


def create_app():
    app_ = Flask(__name__)
    app_.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db.init_app(app_)
    with app_.app_context():
        db.create_all()
    return app_


app = create_app()
migrate = Migrate(app, db)


@app.route('/api', methods=['GET', 'POST'])
@app.route('/api/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    try:
        return db_steps.get_re_entry_by_string(path), 200
    except IndexError:
        return 'There is no such pattern in DB', 400


@app.route('/add_pattern', methods=['POST'])
def add_pattern():
    result = tuple(*request.get_json().items())
    db_steps.add_entry(result[0], result[1])
    return '', 204


@app.route('/clean_db', methods=['GET'])
def clean_db():
    db_steps.clean_db()
    return 'DB was cleaned', 200


@app.route('/get_all', methods=['GET'])
def get_all():
    return str(db_steps.get_add_entries()), 200


if __name__ == '__main__':
    app.run(debug=True)
