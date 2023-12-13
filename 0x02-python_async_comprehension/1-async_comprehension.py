#!/usr/bin/env python3
""" Async Comprehensions"""
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Import 'async_generator' from the '0-async_generator'. 
	Write the coroutine 'async_comprehension' that collects 10 random numbers
	 using an async comprehension over 'async_generator,' then returns the result."""
    return [num async for num in async_generator()]
