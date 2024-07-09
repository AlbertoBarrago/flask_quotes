from flask import Flask

from .favicon import route_favicon
from .quotes import route_external


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.register_blueprint(route_external)
    app.register_blueprint(route_favicon)
    return app
