from flask import Flask
from .routes import route_external


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.register_blueprint(route_external)
    return app
