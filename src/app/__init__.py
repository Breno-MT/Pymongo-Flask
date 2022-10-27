import os
import click
from flask import Flask
from flask_cors import CORS
from flask.cli import with_appcontext
from src.app.config import app_config
from src.app.utils import mongo
from src.app.models.movie import create_collection_movies
from src.app.models.comments import create_collection_comments

app = Flask(__name__)
app.config.from_object(app_config[os.getenv("FLASK_ENV")])
mongo.init_app(app)
mongo_client = mongo.cx.get_database("netflix")

@click.command(name="create_collections")
@with_appcontext
def create_collections():
    create_collection_movies(mongo_client)
    create_collection_comments(mongo_client)

app.cli.add_command(create_collections)

CORS(app)
