import os
from flask import Flask
from flask_cors import CORS
from src.app.config import app_config
from src.app.utils import mongo
from src.app.models.movie import create_collection_movies
from src.app.models.comments import create_collection_comments

app = Flask(__name__)
app.config.from_object(app_config[os.getenv("FLASK_ENV")])
mongo.init_app(app)
mongo_client = mongo.cx.get_database("netflix")

create_collection_movies(mongo_client)
create_collection_comments(mongo_client)

CORS(app)
