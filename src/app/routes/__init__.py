from flask import Flask

from src.app.controllers.movies import movies

def routes(app: Flask):
    app.register_blueprint(movies)
