import os
from flask import Flask
from flask_pymongo import PyMongo
from src.app.config import app_config

mongo = PyMongo(uri=os.getenv("MONGO_URI"))

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(app_config[enviroment])
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo.init_app(app)

    return app

