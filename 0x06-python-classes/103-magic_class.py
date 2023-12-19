#!/usr/bin/python3
import math
"""Import math module for area calculation"""


class MagicClass:
    """Magic class
       Args:
            radius
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculate the area
           Return: 
                 area
        """
        return self.__radius**2 * math.pi

    def circumference(self):
        """Calculate the circumeference
           Return:
                value of circumference
        """
        return 2 * math.pi * self.__radius
