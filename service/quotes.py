# quote_service.py
import os

import mysql
import requests

from service.connect_mysql import connect_mysql


def save_quote_to_db(quote, author):
    try:
        cnx = connect_mysql()
        cursor = cnx.cursor()

        add_quote_query = """
        INSERT INTO quotes (quote, author)
        VALUES (%s, %s)
        """

        cursor.execute(add_quote_query, (quote, author))
        cnx.commit()
        print(f"Quote saved successfully: QUOTE: {quote},  AUTHOR: {author}")
        cursor.close()
        cnx.close()
    except Exception as e:
        print(e)


def get_quotes():
    try:
        response = requests.get(os.getenv('QUOTE_SERVICE'))
        data = response.json()

        if response.status_code != 200 in data:
            return None, 'Could not fetch quote'

        quote = data[0]
        quote_text = quote['q']
        author = quote['a']
        save_quote_to_db(quote_text, author)
        return {
            'quote': quote_text,
            'author': author
        }, None
    except Exception as e:
        return None, str(e)


