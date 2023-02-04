#!/usr/bin/env python3
""" Type-annotation """
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type-annotated function that takes in
    an Iterable as argument and returns a
    List of tuples
    """
    return [(i, len(i)) for i in lst]
