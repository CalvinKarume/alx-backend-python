#!/usr/bin/env python3
"""Calculate the length of each elementt in the input list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples"""
    return [(i, len(i)) for i in lst]
