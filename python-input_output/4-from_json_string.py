#!/usr/bin/python3
"""Task 4"""


import json


def from_json_string(my_str):
    """Return: an object represented"""
    if my_str is None:
        return
    else:
        return json.loads(my_str)
