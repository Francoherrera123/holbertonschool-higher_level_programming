#!/usr/bin/python3
"""This module defines a base to the proyect 'almost_a_circle'"""
import json


class Base:
    """Base class with attributes and init constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that generates a new instance of Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
