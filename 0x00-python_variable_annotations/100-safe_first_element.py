#!/usr/bin/env python3
"""Retrieves the first element of the input list"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of the list"""
    if lst:
        return lst[0]
    else:
        return None
