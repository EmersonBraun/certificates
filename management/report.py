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

def total():
    sql = """
    SELECT COUNT(*) as qtd
    ,SUM(hours_quantity) as total
    FROM certificates 
    """
    try:
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        return cursor.fetchone()

def report():
    sql = """
    SELECT STRFTIME('%Y', completion_date) as year 
    ,COUNT(*) as qtd
    ,SUM(hours_quantity) as total
    FROM certificates 
    GROUP BY 
        STRFTIME('%Y', completion_date)
    ORDER BY completion_date DESC
    """
    try:
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        result = cursor.fetchall()
        t = total()
        columns = ['Year', 'Qtd', 'Total (h)']
        print('|{:<10}|{:<10}|{:<10}|'.format(*columns))
        print('|:{}|:{}|:{}|'.format(9*'-', 9*'-', 9*'-'))
        for r in result:
            print('|{:<10}|{:<10}|{:<10}|'.format(*r))
        print('|{}|{}|{}|'.format(10*'-', 10*'-', 10*'-'))
        print('|Total     |{:<10}|{:<10}|'.format(*t))
        print('\n')


if __name__ == '__main__':
    report()