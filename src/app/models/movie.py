def create_collection_movies(mongo_client):
    movies_validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [ 
            "_id",
            "plot",
            "genres",
            "runtime",
            "cast",
            "num_mflix_comments",
            "title",
            "fullplot",
            "countries",
            "released",
            "directors",
            "rated",
            "awards",
            "lastupdated",
            "year",
            "imdb",
            "type",
            "tomatoes"
        ],
        }
    }

    try:
        mongo_client.create_collection("movies")
        print("Collection Movies created successfully!")
    
    except Exception as e:
        print(f"Something went wrong! {e}")

    mongo_client.command("collMod", "movies", validator=movies_validator)
