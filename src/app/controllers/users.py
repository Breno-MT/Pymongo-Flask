from flask import Blueprint, jsonify
from src.app import mongo


users= Blueprint("user", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def list_all_users():
    
    test_query = mongo.db.users.find({})

    for x in test_query:

        return jsonify(x), 200

    return jsonify(test_query), 200

