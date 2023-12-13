#!/usr/bin/env python3
""" Async Generator """
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Creates the coroutine 'async_generator' that loops 10 times,
	 waits asynchronously for 1 second on each iteration,
	 and yields a random number (0 to 10).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
