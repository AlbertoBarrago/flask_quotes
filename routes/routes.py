# routes.py

from flask import render_template, request, Blueprint, current_app
from service.connect_mysql import get_mysql_connection
from service.get_quotes import get_quotes

route_external = Blueprint('route_external', __name__, template_folder='../templates')


@route_external.route('/favicon.ico', methods=['GET'])
def favicon_ico():
    return current_app.send_static_file('favicon.ico')


@route_external.route('/')
def main():
    return render_template('main/index.html',
                           title='Home',
                           description="Get Quotes from the Internet",
                           isForm=True)


@route_external.route('/quotes', methods=['GET'])
def quotes():
    quote, error = get_quotes()
    if error:
        return render_template('main/index.html',
                               title='Quotes',
                               description="Result",
                               isForm=False,
                               error=error)

    return render_template('main/index.html',
                           title='Quotes',
                           description="Result",
                           isForm=False,
                           quotes=quote)


@route_external.route('/connectMySql', methods=['GET'])
def find_db_password():
    return render_template('main/connect_to_mysql.html',
                           title='Find DB Password',
                           description="Find DB Password",
                           isForm=True)


@route_external.route('/connectMySql', methods=['POST'])
def post_db_password():
    host = request.form['host']
    user = request.form['user']
    database = request.form['database']
    password = request.form['password']
    connection = get_mysql_connection(
        host=host,
        user=user,
        database=database,
        password=password
    )
    if connection:
        return render_template('main/connect_to_mysql.html',
                               title='Find DB Password',
                               description="Find DB Password",
                               isForm=False,
                               success=True)
    else:
        return render_template('main/connect_to_mysql.html',
                               title='Find DB Password',
                               description="Find DB Password",
                               isForm=False,
                               error="Password not found")
