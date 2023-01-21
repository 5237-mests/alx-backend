#!/usr/bin/env python3
"""Module for task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end of page selected."""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
