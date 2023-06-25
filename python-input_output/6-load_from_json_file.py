#!/usr/bin/python3
"""Task 6"""
import json


def load_from_json_file(filename):
    """creates an object from a Json file"""
    with open(filename, 'r') as new_obj:
        return json.load(new_obj)
