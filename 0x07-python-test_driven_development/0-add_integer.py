#!/usr/bin/python3
"""No module import"""


def add_integer(a, b=98):
    """Add two number
        add - function for adding two nummber
        @a: int or float
        @b: int or float
        @return: a+b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return (a + b)
