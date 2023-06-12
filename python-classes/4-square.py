#!/usr/bin/python3
"""Task 4"""


class Square:
    """A class representanding a Square"""
    


    def __init__(self, size=0):
             self.__size = size
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size * self.__size)
