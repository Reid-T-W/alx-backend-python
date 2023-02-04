#!/usr/bin/env python3
""" Type-annotated function that returns a function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type-annotated function that takes in a
    float as argument and returns a function
    """
    return (lambda a: a * multiplier)
