import json

import requests


def send_pattern(pattern, payload):
    return requests.post('http://localhost:5000/add_pattern', json={pattern: json.dumps(payload)})


if __name__ == '__main__':
    send_pattern('localhost\d', {'result': True})
