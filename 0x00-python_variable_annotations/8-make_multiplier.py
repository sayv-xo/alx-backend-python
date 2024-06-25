#!/usr/bin/env python3
"""Returns a multiplier function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by multiplier

    Args: multiplier: the multiplier

    Returns: function to multiply
    """
    return lambda x: x * multiplier
