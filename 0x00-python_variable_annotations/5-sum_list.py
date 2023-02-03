#!/usr/bin/env python3
""" Complex type-annotations """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sum_list function with complex annotation
    arguments take list of floats
    returns the sum of floats
    """
    sum = 0
    for num in input_list:
        sum += num
    return sum
