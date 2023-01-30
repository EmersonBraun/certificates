#!/usr/bin/python3
def validate_field(placeholder):
    data = input(placeholder)
    while not data:
        print('This field is required')
        data = input(placeholder)
    return data

