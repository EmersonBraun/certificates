#!/usr/bin/python3
from sys import exit
import os
from utils import clear
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


def delete():
    idc = input('What id do you want to delete? ')
    sql = 'DELETE FROM certificates WHERE id = ?'
    try:
        cursor.execute(sql, idc)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'{idc} deleted')


def count_all():
    sql = 'SELECT COUNT(*) FROM certificates ORDER BY completion_date ASC'
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
        print(f'{qt} registry')

        sql = """
            SELECT institution, description, hours_quantity, completion_date 
            FROM certificates
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


def report():
    pass


def print_menu():
    print(10 * '-', 'Certificate Management', 10 * '-')
    print('1. Add')
    print('2. List')
    print('3. Report')
    print('4. Delete')
    print('5. Exit')
    print(67 * '-')


def main():
    while True:
        print_menu()
        choice = int(input("Enter your choice [1-5]:"))
        if choice == 1:
            clear()
            add()
        elif choice == 2:
            clear()
            list_all()
        elif choice == 3:
            clear()
            report()
        elif choice == 4:
            clear()
            delete()
        elif choice == 5:
            print("Exit")
            conn.close()
            exit(1)
            break
        else:
            clear()
            print("Wrong option selection.")


if __name__ == '__main__':
    create_table()
    main()
