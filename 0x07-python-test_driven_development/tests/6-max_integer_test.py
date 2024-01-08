#!/usr/bin/python3
""" Module to test maxintergwer in a list"""

import unittest

max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        res =max_integer([1, 2, 3, 4])
        self.assertEqual(res, 4)
