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
    print('Connected')
    cursor = conn.cursor()


def add():
    institution = input('Institution: ')
    description = input('Description: ')
    hours_quantity = input('Quantity of hours: (00.00)')
    completion_date = input('Date of completion (yyyy-mm-dd): ')

    bind = (institution, description, hours_quantity, completion_date)

    sql = """
        INSERT INTO certificates
            (institution, description, hours_quantity, completion_date)
        VALUES (?, ?, ?, ?)
    """
    try:
        cursor.execute(sql, bind)
        conn.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
        conn.rollback()
    else:
        print(67 * '=')
        print(f'ID {cursor.lastrowid} inserted')
        print(67 * '=')
        print()
