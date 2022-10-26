import json
from bson import json_util
from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client


movies = Blueprint("movies", __name__, url_prefix="/movies")

@movies.route("/", methods=["GET"])
def list_all_movies():
    
    movies = mongo_client.movies.aggregate([
        {
            "$match": {
                "type": "Movie"
            }
        }
    ])

    return Response(
        response=json_util.dumps({"records": movies}),
        status=200,
        mimetype="application/json"
    )
