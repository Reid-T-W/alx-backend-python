#!/usr/bin/env python3
""" Async coroutine that collects data from async generator """
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    result = []
    async for num in async_generator():
        result.append(num)
    return result
