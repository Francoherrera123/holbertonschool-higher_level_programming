#!/usr/bin/python3
"""Task 9"""


class Student():
    """Class Student with attributes"""

    def __init__(self, first_name, last_name, age):
        """To create a new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def ro_json(self):
        """Retriebves a directory representation of a student instance"""
        return self.__dict__
