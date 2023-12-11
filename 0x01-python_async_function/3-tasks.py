#!/usr/bin/env python3
"""Async Tasks"""


import importlib
import asyncio

MODULE_NAME = '0-basic_async_syntax'
module = importlib.import_module(MODULE_NAME)
wait_random = getattr(module, 'wait_random')


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Import the wait_random function from the '0-basic_async_syntax' module.
	 Create a regular function, task_wait_random, which takes
	 an integer max_delay and returns an asyncio.Task."""
    return asyncio.create_task(wait_random(max_delay))
