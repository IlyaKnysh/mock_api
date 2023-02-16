# Requirements:
- python3

# Install dependencies:
pip install -r requirements.txt

# Start API:
You can set api path to API_PATH system variable. By default, API_PATH=api

    $ python app.py

or

    $ sh start.sh

# Available Endpoints:
/get_all - get all db entries

/clean_db - recreate db

/add_pattern - add pattern to db

/api/... - will return response based on path pattern

# Examples of use
Add response for get request v1/patients/{id} for any id

    $ curl -XPOST -H "Content-type: application/json" -d '{"path": "v1/patients/\\d*", "payload": {"some_response_attrib":1}}' 'http://127.0.0.1:5000/add_pattern'

Check that mock response was added

    $ curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:5000/api/v1/patients/2'

Get log of requests

    $ curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:5000/get_all'

Clean DB with patterns

    $ curl -XGET -H "Content-type: application/json" 'http://127.0.0.1:5000/clean_db'