#!/usr/bin/python3
"""Task 2"""


class Square:
    """A class representanding a Square"""
    def __init__(self, size=None):
        if type(size) is not int:
            raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
    pass
