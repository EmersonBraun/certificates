#!/usr/bin/python3
from datetime import date
from list_all import get_list

def update():
    print("Create or update README.MD")
    f = open('../README.MD','w', encoding="utf8")
    content = []

    print("Header")
    content.append("# List of certificates\n")

    print("Date of update")
    content.append(f'## Updated: {date.today()}\n')

    print("Get list of certificates")
    result = get_list()
    columns = ['Name', 'Description', 'Hours', 'Date']
    content.append('|{:<20}|{:<60}|{:<5}|{:<10}|\n'.format(*columns))
    content.append('|:{}|:{}|:{}|:{}|\n'.format(19*'-', 59*'-', 4*'-', 9*'-'))
    for r in result:
        content.append('|{:<20}|{:<60}|{:<5}|{:<10}|\n'.format(*r))

    content.append('\n\n')
    f.writelines(content)
    f.close()

if __name__ == '__main__':
    update()