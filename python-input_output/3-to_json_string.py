#!/usr/bin/python3
"""Task 3"""


import json


def to_json_string(my_obj):
    """Return: the json representation of an object"""
    if my_obj is None:
        return
    else:
        return json.dumps(my_obj)
