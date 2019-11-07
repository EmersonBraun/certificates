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


def count_all():
    sql = 'SELECT COUNT(*) FROM certificates '
    try:
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        row = cursor.fetchone()
        return int(row[0])


def list_all():
    qt = count_all()
    if qt == 0:
        print('Nothing inserted')
    else:
        sql = """
            SELECT institution, description, hours_quantity
            , completion_date FROM certificates
            ORDER BY completion_date DESC
            """
        try:
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
        else:
            columns = ['Name', 'Description', 'Hours', 'Date']
            print('|{:<20}|{:<60}|{:<5}|{:<10}|'.format(*columns))
            print('|:{}|:{}|:{}|:{}|'.format(19*'-', 59*'-', 4*'-', 9*'-'))
            for result in cursor.fetchall():
                print('|{:<20}|{:<60}|{:<5}|{:<10}|'.format(*result))
            print('\n\n')


if __name__ == '__main__':
    list_all()
