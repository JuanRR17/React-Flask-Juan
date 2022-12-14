"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import request, jsonify, url_for, Blueprint
from api.models import db, User

api = Blueprint('api', __name__)


@api.route('/hello', methods=['GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/members', methods=['GET'])
def members():

    response_body = {
        "members": ["Member 1","Member 2","Member 3","Member 4"]
    }

    return jsonify(response_body), 200