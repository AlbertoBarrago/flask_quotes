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


def connect_mysql():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=config.get('host'),
            user=config.get('user'),
            password=config.get('password'),
            database=config.get('database'),
        )
        if connection.is_connected():
            return print(f"Connected to MySQL Server version {connection.get_server_info()}")
    except Error as e:
        print(f"Failed to connect | Error: {e}")
    finally:
        if connection and connection.is_connected():
            # connection.close()
            print("Connected to MySQL")
    print("Password not found after maximum attempts")
    return None
