from flask import Flask, jsonify, request
import http.client
import gzip
import json

from env import API_HOST, API_KEY

app = Flask(__name__)

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
    json_response = json.loads(decoded_decompressed_data)
    return json_response

@app.route('/status', methods=['GET'])
def get_status():
    return get_request('/status')

@app.route('/leagues', methods=['GET'])
def get_leagues():
    return get_request('/leagues')

if __name__ == '__main__':
    app.run(debug=True)
