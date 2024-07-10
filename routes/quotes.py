from flask import render_template, Blueprint
from service.quotes import get_new_quotes_and_read_first, get_all_quotes

route_external = Blueprint('route_external', __name__, template_folder='../templates')


@route_external.route('/')
def main():
    return render_template('main/index.html',
                           title='Home',
                           description="Get Quotes from the Internet",
                           isForm=True)


@route_external.route('/quotes', methods=['GET'])
def quotes():
    quote, error = get_new_quotes_and_read_first()
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


@route_external.route('/quotes/get_quotes', methods=['GET'])
def get_quotes():
    quotes_list = get_all_quotes()
    print(quotes_list)
    return render_template('main/quotes.html',
                           title='Quotes',
                           description="Inspirational Quotes",
                           quotes=quotes_list)
