#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """Empry classs that defines a new instance"""
    pass

    def area(self):
        """calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
