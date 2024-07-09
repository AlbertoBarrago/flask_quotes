# connect_mysql.py
import string

import mysql
from mysql.connector import Error


def get_mysql_connection(host, user, database, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(f"Success: Password found - {password}")
            return password
    except Error as e:
        print(f"Failed to connect using password: {password} | Error: {e}")
    finally:
        if connection and connection.is_connected():
            # connection.close()
            print("Connected to MySQL")
    print("Password not found after maximum attempts")
    return None
