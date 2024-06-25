#!/usr/bin/env python3
"""Sums of a list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums list of float

    Args:
        input_list: list of floats to sum

    Returns:
        sum of the values in the list
    """
    return sum(input_list)
