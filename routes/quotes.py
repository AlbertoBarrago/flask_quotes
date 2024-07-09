from flask import render_template, Blueprint
from service.quotes import get_quotes

route_external = Blueprint('route_external', __name__, template_folder='../templates')


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
