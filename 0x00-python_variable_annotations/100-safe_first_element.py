#!/usr/bin/env python3
""" Type-annotated function """
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type-annotated function that takes in
    Sequence as argument and returns either of
    type Any or None
    """
    if lst:
        return lst[0]
    else:
        return None
