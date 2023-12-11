#!/usr/bin/env python3
"""Measure the Runtime"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
       """imports the wait_n coroutine from a previous file and defines measure_time,
 a function that measures the total execution time for wait_n(n, max_delay)"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
