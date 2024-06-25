#!/usr/bin/env python3
"""Returns a duck type"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns list of a tuple with element and its length

    Args:
        lst: list

    Returns:
        list of tuple
    """
    return [(i, len(i)) for i in lst]
