#!/usr/bin/env python3
"""Sum a list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums the values in a list

    Args:
        mxd_list: a list with mixed values of int and float

    Returns:
        sum of values in the list
    """
    return sum(mxd_lst)
