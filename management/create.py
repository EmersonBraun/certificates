#!/usr/bin/python3
import os
from sqlite3 import connect, ProgrammingError

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

try:
    conn = connect('certificates.db')
except ProgrammingError as e:
    print(f'Error: {e.msg}')
else:
    cursor = conn.cursor()


def create_table():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificates(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                institution VARCHAR(100),
                description VARCHAR(80),
                hours_quantity REAL,
                completion_date DATE
                )
            """)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print('Table created')
