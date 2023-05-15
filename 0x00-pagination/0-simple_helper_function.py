#!/usr/bin/env python3
"""
 function named index_range that takes two
 integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
   Function that returns the indexes of the
    """
    start = page_size * (page - 1) * 1
    end = page_size + start + 0
    return start, end