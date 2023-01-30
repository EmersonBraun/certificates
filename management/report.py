#!/usr/bin/python3
import os
from db import total, report_data

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

def report():
    try:
        t = total()
        if t[0] == 0:
            print('Nothing inserted')
        else:
            result = report_data()
            columns = ['Year', 'Qtd', 'Total (h)']
            print('|{:<10}|{:<10}|{:<10}|'.format(*columns))
            print('|:{}|:{}|:{}|'.format(9*'-', 9*'-', 9*'-'))
            for r in result:
                print('|{:<10}|{:<10}|{:<10}|'.format(*r))
            print('|{}|{}|{}|'.format(10*'-', 10*'-', 10*'-'))
            print('|Total     |{:<10}|{:<10}|'.format(*t))
            print('\n')
    except Exception as e:
        print(f'Error: {e}')



if __name__ == '__main__':
    report()