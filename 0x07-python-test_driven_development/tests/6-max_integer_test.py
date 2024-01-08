#!/usr/bin/python3
""" Module to test maxintergwer in a list"""

import unittest

max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        """Test list is not empty"""
        res = max_integer([1, 2, 3, 4])
        self.assertEqual(res, 4)

    def test_empyt_list(self):
        """Test empty list to return None"""
        res  = max_integer([])
        self.assertEqual(res, None)
