#!/usr/bin/python3
"""Task 5"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using json representation"""
    if my_obj is None:
        return
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            to_write = json.dumps(my_obj)
            file.write(to_write)
