from flask import Flask

from app.controllers.movies import movies

def routes(app: Flask):
    app.register_blueprint(movies)
