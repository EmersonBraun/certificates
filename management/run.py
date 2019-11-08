#!/usr/bin/python3
from sys import exit
import os
from utils import clear
from sqlite3 import connect, ProgrammingError
# functions
from add import add
from create import create_table
from delete import delete
from list_all import list_all
from menu import print_menu
from report import report
from update_readme import update

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

try:
    conn = connect('certificates.db')
except ProgrammingError as e:
    print(f'Error: {e.msg}')
else:
    cursor = conn.cursor()


def main():
    while True:
        print_menu()
        choice = int(input("Enter your choice [1-6]:"))
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
            update()
        elif choice == 5:
            clear()
            delete()
        elif choice == 6:
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
