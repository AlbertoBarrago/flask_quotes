# quote_service.py

from flask import jsonify
import requests


def get_quotes():
    try:
        response = requests.get('https://zenquotes.io/api/quotes')
        data = response.json()

        if response.status_code != 200 in data:
            return None, 'Could not fetch quote'

        quote = data[0]
        return {
            'quote': quote['q'],
            'author': quote['a']
        }, None
    except Exception as e:
        return None, str(e)
