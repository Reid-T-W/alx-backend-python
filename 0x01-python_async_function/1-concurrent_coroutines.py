#!/usr/bin/env python3
""" Execute multiple coroutines at the same time """
from typing import Callable


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> [float]:
    delays = []
    delays = [await wait_random(max_delay) for i in range(n)]
    return delays
