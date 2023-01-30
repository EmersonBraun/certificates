#!/usr/bin/python3
import os
from sqlite3 import connect, ProgrammingError
from db import count_all, get_list

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

try:
    conn = connect('certificates.db')
except ProgrammingError as e:
    print(f'Error: {e.msg}')
else:
    cursor = conn.cursor()


def list_all():
    qt = count_all()
    if qt == 0:
        print('Nothing inserted')
    else:
        result = get_list()
        columns = ['Name', 'Description', 'Hours', 'Date']
        print('|{:<20}|{:<60}|{:<5}|{:<10}|'.format(*columns))
        print('|:{}|:{}|:{}|:{}|'.format(19*'-', 59*'-', 4*'-', 9*'-'))
        for r in result:
            print('|{:<20}|{:<60}|{:<5}|{:<10}|'.format(*r))
        print('\n\n')


if __name__ == '__main__':
    list_all()
