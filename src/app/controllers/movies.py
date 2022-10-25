import json
from bson import json_util
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client


movies = Blueprint("movies", __name__, url_prefix="/movies")

@movies.route("/", methods=["GET"])
def list_all_movies():
    
    collection_names = mongo_client.list_collection_names()

    return Response(
        response=json.dumps(collection_names),
        status=200,
        mimetype="application/json"
    )
