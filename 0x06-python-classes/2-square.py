#!/usr/bin/python3

"""Write a description module here"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initialises the data
           Args:
                size: the size of the square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
