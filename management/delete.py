#!/usr/bin/python3
import os
from sqlite3 import connect, ProgrammingError
from db import delete

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

try:
    conn = connect('certificates.db')
except ProgrammingError as e:
    print(f'Error: {e.msg}')
else:
    cursor = conn.cursor()


def delete():
    idc = input('What id do you want to delete? ')
    sql = delete(idc)
    try:
        cursor.execute(sql, idc)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'{idc} deleted')
