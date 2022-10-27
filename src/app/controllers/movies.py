import json
from bson import ObjectId, json_util
from flask import Blueprint, request
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

@movies.route("/add_movie", methods=["POST"])
def add_a_new_movie():

    new_movie = request.get_json()

    mongo_client.movies.insert_one(new_movie)

    return Response(
        response=json_util.dumps({"records": new_movie}),
        status=201,
        mimetype="application/json"
    )

@movies.route("/update_movie/<string:id>", methods=["PATCH"])
def update_a_movie(id):

    update_movie = request.get_json()

    object_id = ObjectId(id)

    mongo_client.movies.update_one({"_id": object_id}, {"$set": update_movie})

    return Response(
        response=json_util.dumps({"records": update_movie}),
        status=204,
        mimetype="application/json"
    )

@movies.route("/delete_movie/<string:id>", methods=["DELETE"])
def delete_a_movie(id):

    object_id = ObjectId(id)

    mongo_client.movies.delete_one({"_id": object_id})

    return Response(
        response=json_util.dumps({"records": "Movie deleted successfully!"}),
        status=204,
        mimetype="application/json"
    )

