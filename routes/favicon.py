from flask import Blueprint, current_app

route_favicon = Blueprint('route_favicon', __name__, template_folder='../templates')


@route_favicon.route('/favicon.ico', methods=['GET'])
def favicon_ico():
    return current_app.send_static_file('favicon.ico')
