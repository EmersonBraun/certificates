#!/usr/bin/python3
import os
from db import connect_db, create_table

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

def clear_db():
    try:
        conn = connect_db()
        conn.execute('DROP TABLE IF EXISTS certificates')
        create_table()
    except Exception as e:
        print(f'Error: {e}')
    else:
        print('Database cleared')

if __name__ == '__main__':
    clear_db()

