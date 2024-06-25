#!/usr/bin/env python3
"""Return a tuple of string and int/float"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and root of a number

    Args:
        k: a string
        v: the number to square

    Returns:
        a tuple of string k, and square of thr number v.
    """
    return (k, pow(v, 2))
