#!/usr/bin/env python3
""" Async coroutine that collects data from async generator """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Async coroutine that collects data from async generator """
    result = []
    result = [num async for num in async_generator()]
    return result
