#!/usr/bin/env python3
"""utils tests module"""

import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Union, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """Test the `access_nested_map` function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
    ) -> None:
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception
    ) -> None:
        """test access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
