from flask import Flask, render_template, request

from service.get_password import test_random_passwords
from service.get_quotes import get_quotes

app = Flask(__name__)


@app.route('/favicon.ico', methods=['GET'])
def favicon_ico():
    return app.send_static_file('favicon.ico')


@app.route('/')
def main():
    return render_template('main/index.html',
                           title='Home',
                           description="Get Quotes from the Internet",
                           isForm=True)


@app.route('/quotes', methods=['GET'])
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


@app.route('/findDbPassword', methods=['GET'])
def find_db_password():
    return render_template('main/findDbPassword.html',
                           title='Find DB Password',
                           description="Find DB Password",
                           isForm=True)


@app.route('/findDbPassword', methods=['POST'])
def post_db_password():
    host = request.form['host']
    user = request.form['user']
    database = request.form['database']
    print(host,user, database)
    password = test_random_passwords(
        host=host,
        user=user,
        database=database,
    )
    if password:
        return render_template('main/findDbPassword.html',
                               title='Find DB Password',
                               description="Find DB Password",
                               isForm=False,
                               password=password)
    else:
        return render_template('main/findDbPassword.html',
                               title='Find DB Password',
                               description="Find DB Password",
                               isForm=False,
                               error="Password not found")


if __name__ == '__main__':
    app.run()
