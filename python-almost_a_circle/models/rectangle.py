#!/usr/bin/python3
"""Module that creates a class 'Rectangle' that inherits from class 'Base'"""
from models.base import Base


class Rectangle(Base):
    """New class, inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor that creates a new instance"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ To get the private width attribute: getter """
        return self.__width

    @property
    def height(self):
        """ To get the private height attribute: getter """
        return self.__height

    @property
    def x(self):
        """ To get the private x attribute: getter """
        return self.__x

    @property
    def y(self):
        """ To get the private y attribute: getter """
        return self.__y
