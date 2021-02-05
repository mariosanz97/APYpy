from flask import Flask, jsonify
import requests
import gzip
import json
from gzip import decompress
from json import loads

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/json/minor')
def api_get():
    json_cont= api_callback()
    return jsonify(json_cont)

def api_callback():
    print("entramos")
    #descarga json.gz neeas, y descomprime
    #r = requests.get('https://minorplanetcenter.net/Extended_Files/nea_extended.json.gz')
    #cont= gzip.decompress(r.content)
    r = requests.get('https://www.minorplanetcenter.net/Extended_Files/neocp.json')
    json_content= r.json()
    print(json.dumps(json_content, indent=2))
    return json_content
    



