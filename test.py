from flask import Flask, jsonify, request, Response
from bson import json_util, ObjectId
from pymongo import MongoClient
import json

# setup mongodb
client = MongoClient("localhost", 27017)
db = client.test

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome_screen():
    return '<html><body><h1>Welcome</h1></body></html>'


@app.route('/save', methods=['POST'])
def save_data():
    user_data = db.users.insert_one({'name': 'Ganesh', 'surname': 'Avhad'})
    return Response('saved', status=201, mimetype='application/json')


@app.route('/get', methods=['GET'])
def get_data():
    user_data = db.users.find_one({})
    return Response(json_util.dumps(user_data), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
