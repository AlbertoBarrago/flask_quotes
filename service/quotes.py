# quote_service.py
import os
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


def get_new_quotes_and_read_first():
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


def get_all_quotes():
    try:
        cnx = connect_mysql()
        cursor = cnx.cursor(dictionary=True)

        get_quotes = """
         SELECT author, quote FROM quotes ORDER BY quote DESC
        """
        cursor.execute(get_quotes)
        list_quotes = cursor.fetchall()

        cursor.close()
        cnx.close()

        return list_quotes
    except Exception as e:
        print(e)
