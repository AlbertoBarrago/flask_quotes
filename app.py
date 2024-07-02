from flask import Flask, render_template

from service.get_quotes import get_quotes

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main/index.html', title='Home', description="Get Quotes from the Internet", isForm=True)


@app.route('/quotes', methods=['GET'])
def quotes():
    quote, error = get_quotes()
    if error:
        return render_template('main/index.html', title='Quotes', description="Result", isForm=False, error=error)

    return render_template('main/index.html', title='Quotes', description="Result", isForm=False, quotes=quote)


if __name__ == '__main__':
    app.run()
