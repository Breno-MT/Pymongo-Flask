import json
from bson import json_util
from flask import Blueprint
from flask.wrappers import Response
from src.app import DB


users= Blueprint("user", __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def list_all_users():
    
    dbname = DB.cx.get_database("BusPeople")
    collection_name = dbname["passagem"]

    user = collection_name.find()


    return Response(
        response=json.dumps(json_util.dumps(user)),
        status=200,
        mimetype="application/json"
    )
