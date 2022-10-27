def create_collection_movies(mongo_client):
    movies_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["type", "title", "release_year", "description", "cast"],
            "properties": {
                "type": {
                    "bsonType": "string",
                    "description": "If its either a Movie or TV Show",
                    "enum": ["Movie", "TV Show"]
                },
                "title": {
                    "bsonType": "string",
                    "description": "Movies or TV Shows title"
                },
                "release_year": {
                    "bsonType": "int",
                    "description": "Movies or TV Shows release year"
                },
                "description": {
                    "bsonType": "string",
                    "description": "Description of the Movies or TV Shows"
                },
                "cast": {
                    "bsonType": "array",
                    "description": "Movie cast",
                    "items": {
                        "bsonType": "string",
                        "description": "Person from the Movie or TV Show"
                    }
                }
            }
        }
    }

    try:
        mongo_client.create_collection("movies")
        print("Database created successfully!")
    
    except Exception as e:
        print(f"Something went wrong! {e}")

    mongo_client.command("collMod", "movies", validator=movies_validator)
