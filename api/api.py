import time

from flask import Flask, jsonify, request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='../build', static_url_path='/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://test:test@localhost:5405/insurance'
db = SQLAlchemy(app)
ma = Marshmallow(app)

import broker_service


@app.errorhandler(404)
def not_found(e):
    return app.send_static_file('index.html')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}


@app.route('/api/sign-up', methods=['POST'])
def sign_up():
    data = request.json
    return broker_service.signup(data)


@app.route('/api/brokers', methods=['GET'])
def get_brokers():
    return broker_service.get_brokers()
