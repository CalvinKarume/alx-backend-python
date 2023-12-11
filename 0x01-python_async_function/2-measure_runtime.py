#!/usr/bin/env python3
"""Measure the runtime"""

import importlib
import asyncio
import time

MODULE_NAME = '1-concurrent_coroutines'
module = importlib.import_module(MODULE_NAME)
wait_n = getattr(module, 'wait_n')


def measure_time(n: int, max_delay: int) -> float:
   """imports the wait_n coroutine from a previous file and defines measure_time,
 a function that measures the total execution time for wait_n(n, max_delay)""" 
        
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 3
    avg_time = measure_time(n, max_delay)
    print(f"Average time per operation: {avg_time} seconds")

