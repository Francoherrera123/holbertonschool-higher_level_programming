#!/usr/bin/python3
"""Task 2"""


def write_file(filename="", text=""):
    """writes a string to text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
