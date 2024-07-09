# connect_mysql.py
from pathlib import Path

import mysql
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'raise_on_warnings': True,
}

create_table_query = """
CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quote TEXT NOT NULL,
    author VARCHAR(255),
    date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""


def connect_mysql():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Failed to connect | Error: {e}")
    return None


def close_connection(connection):
    try:
        if connection.is_connected():
            server_info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.close()
            connection.close()
            print(f"Connected to MySQL Server version {server_info}")
            return True
    except Error as e:
        print(f"Failed to close connection | Error: {e}")
        return False
