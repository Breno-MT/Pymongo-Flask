def create_collection_cast(mongo_client):
    cast_validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["full_name"],
            "properties": {
                "full_name": {
                    "bsonType": "string",
                    "description": "O nome da pessoa do elenco"
                },
            },
        }
    }

    try:
        mongo_client.create_collection("cast")
    except Exception as e:
        print(e)

    mongo_client.command("collMod", "cast", validator=cast_validator)