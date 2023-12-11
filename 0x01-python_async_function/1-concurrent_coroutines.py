#!/usr/bin/env python3
"""executing multiple coroutines at the same time with async"""

import importlib
import asyncio
from typing import List


MODULE_NAME = '0-basic_async_syntax'
module = importlib.import_module(MODULE_NAME)
wait_random = getattr(module, 'wait_random')


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
 an async function, wait_n, that concurrently
 spawns wait_random with specified delays (max_delay) n times
     """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
