#!/usr/bin/python3
"""Task 2"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
