import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from src.app.config import app_config

DB = PyMongo(uri=os.getenv("MONGO_URI"))

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(app_config[enviroment])
    DB.init_app(app)
    CORS(app)

    return app

