#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    interger shold be printed follow by new line
    type is not allowed
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print(f"Exception: {err}", file=sys.stderr)
        return False
