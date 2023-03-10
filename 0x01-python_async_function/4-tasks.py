#!/usr/bin/env python3
""" Execute multiple coroutines at the same time """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines """
    delays = []
    results = []
    delays = [task_wait_random(max_delay) for i in range(n)]
    for res in asyncio.as_completed(delays):
        results.append(await res)
    return results
