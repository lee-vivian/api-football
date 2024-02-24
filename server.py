from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import http.client
import gzip
import json

from env import API_HOST, API_KEY

app = Flask(__name__)

allowed_origins = [
    "http://localhost:4200",
]

cors = CORS(app, resources={r"*": {"origins": allowed_origins}})

app.config['CORS_HEADERS'] = 'Content-Type'

def get_headers():
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'x-rapidapi-host': API_HOST,
        'x-rapidapi-key': API_KEY,
    }
    return headers

def get_request(endpoint):
    conn = http.client.HTTPSConnection(API_HOST)
    headers = get_headers()
    conn.request('GET', endpoint, headers=headers)
    response = conn.getresponse()
    response_data = response.read()
    decompressed_data = gzip.decompress(response_data)
    decoded_decompressed_data = decompressed_data.decode('utf-8')
    json_response = json.loads(decoded_decompressed_data)['response']
    return json_response

@app.route('/status', methods=['GET'])
def get_status():
    return get_request('/status')

@app.route('/leagues', methods=['GET'])
def get_leagues():
    return get_request('/leagues')

if __name__ == '__main__':
    app.run(debug=True)
