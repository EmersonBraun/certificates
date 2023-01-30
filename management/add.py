#!/usr/bin/python3
import os
from sqlite3 import ProgrammingError
from validate_field import validate_field
from db import insert

if not os.path.exists('certificates.db'):
    with open('certificates.db', 'w'):
        pass

def add():
    institution = validate_field('Institution: ')
    description = validate_field('Description: ')
    hours_quantity = validate_field('Hours quantity: ')
    completion_date = validate_field('Completion date: ')

    try:
        lastrowid = insert(institution, description, hours_quantity, completion_date)
        if lastrowid:
            print(67 * '=')
            print(f'ID {lastrowid} inserted')
            print(67 * '=')
            print()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')

