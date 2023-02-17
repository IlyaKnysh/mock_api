import os

SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
API_PATH = os.environ.get('API_PATH', 'api')