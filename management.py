#!/usr/bin/python3
import sys
from os import system, name
from sqlite3 import connect, ProgrammingError

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


def edit():
    idc = input('What id do you want to update? ')
    institution = input('Institution: ')
    description = input('Description: ')
    hours_quantity = input('Quantity of hours: (00.00)')
    completion_date = input('Date of completion (yyyy-mm-dd): ')

    bind = (institution, description, hours_quantity, completion_date, idc)

    sql = """
    UPDATE certificates SET
        institution = ?, description = ?
        , hours_quantity = ?, completion_date = ?
    WHERE id = ?
    """
    try:
        cursor.execute(sql, bind)
        conn.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
        conn.rollback()
    else:
        print(67 * '=')
        print('Updated')
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

        sql = 'SELECT * FROM certificates'
        try:
            cursor.execute(sql)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
        else:
            columns = ['#', 'Name', 'Description', 'Hours', 'Date']
            print('|{:<3}|{:<25}|{:<25}|{:<5}|{:<10}|'.format(*columns))
            print('|:--|:', 22*'-', '|:', 22 *
                  '-', '|:', 2*'-', '|:', 7*'-', '|')
            for result in cursor.fetchall():
                print('|{:<3}|{:<25}|{:<25}|{:<5}|{:<10}|'.format(*result))
            print('\n\n')


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def print_menu():
    print(10 * '-', 'Certificate Management', 10 * '-')
    print('1. Add')
    print('2. Edit')
    print('3. Delete')
    print('4. List')
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
            edit()
        elif choice == 3:
            clear()
            delete()
        elif choice == 4:
            clear()
            list_all()
        elif choice == 5:
            print("Exit")
            conn.close()
            sys.exit(1)
            break
        else:
            clear()
            print("Wrong option selection.")


if __name__ == '__main__':
    create_table()
    main()
