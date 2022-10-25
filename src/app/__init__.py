import os
from flask import Flask
from flask_cors import CORS
from src.app.config import app_config
from src.app.utils import mongo

app = Flask(__name__)
app.config.from_object(app_config[os.getenv("FLASK_ENV")])
mongo.init_app(app)
mongo_client = mongo.db

CORS(app)


