#!/usr/bin/env python3
""" Asynchronous coroutine """
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous corotine that returs a random delay """
    random_delay = random.uniform(0, max_delay)
    return random_delay
