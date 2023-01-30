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

def connect_db():
    try:
        conn = connect('certificates.db')
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print('Connected')
        return conn.cursor()

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

def insert(institution, description, hours_quantity, completion_date):
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
        return cursor.lastrowid
    
def count_all():
    sql = 'SELECT COUNT(*) FROM certificates '
    try:
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        row = cursor.fetchone()
        return int(row[0])


def get_list():
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
        return cursor.fetchall()
    
def update(idc, institution, description, hours_quantity, completion_date):
    bind = (institution, description, hours_quantity, completion_date, idc)
    sql = """
        UPDATE certificates
        SET institution = ?,
            description = ?,
            hours_quantity = ?,
            completion_date = ?
        WHERE id = ?
    """
    try:
        cursor.execute(sql, bind)
        conn.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
        conn.rollback()
    else:
        print(f'{idc} updated')

def delete(idc):
    sql = 'DELETE FROM certificates WHERE id = ?'
    try:
        cursor.execute(sql, idc)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'{idc} deleted')

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
    
def report_data():
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
        return cursor.fetchall()
