#!/usr/bin/env python3
""" Async Generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async Generator """
    for i in range(10):
        await asyncio.sleep(1)
        random_no = random.uniform(0, 10)
        yield random_no
