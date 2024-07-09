from flask import Flask

from service.connect_mysql import connect_mysql
from .favicon import route_favicon
from .quotes import route_external


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.register_blueprint(route_external)
    app.register_blueprint(route_favicon)
    connect_mysql()
    return app

