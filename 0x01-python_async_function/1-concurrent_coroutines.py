#!/usr/bin/env python3
""" Execute multiple coroutines at the same time """
from typing import Callable
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> [float]:
    """ Execute multiple coroutines """
    delays = []
    results = []
    delays = [wait_random(max_delay) for i in range(n)]
    for res in asyncio.as_completed(delays):
        results.append(await res)
    return results
