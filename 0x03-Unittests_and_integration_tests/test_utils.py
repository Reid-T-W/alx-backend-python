#!/usr/bin/env python3
"""
Test class for utils.py
"""
import unittest
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for utils.py
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test for the test_access_nested_map method """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test if key error is raised for the test_access_nested_map method
        """
        with self.assertRaises(KeyError, msg='a') as error:
            access_nested_map(nested_map, path)
        # self.assertEqual(error.exception, KeyError('a'))
