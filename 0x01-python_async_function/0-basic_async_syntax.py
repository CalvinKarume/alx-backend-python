#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """An async function wait_random(max_delay=10) that
    generates a random delay (0 to max_delay seconds)
    and returns it after asynchronous sleep."""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
