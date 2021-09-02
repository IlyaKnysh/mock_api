# Requirements:
- python3

# Install dependencies:
pip install -r requirements.txt

# Start API:
python app.py

# Endpoints:
/get_all - get all db entries

/clean_db - recreate db

/add_pattern - add pattern to db. Example:

    $ requests.post('http://localhost:5000/add_pattern', json={'localhost\d': json.dumps({'result': True})})

/api/... - will return response based on path pattern