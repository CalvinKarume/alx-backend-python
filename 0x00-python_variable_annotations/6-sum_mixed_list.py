#!/usr/bin/env python3
"""Define a function sum_mixed_list that takes a list (mxd_lst) of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return The sum of the numbers in 'mxd_lst' as a float"""
    return sum(mxd_lst)
