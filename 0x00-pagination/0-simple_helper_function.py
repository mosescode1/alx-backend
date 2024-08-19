#!/usr/bin/env python3
"""Module"""


def index_range(page, page_size):
    "index Method"
    start = int(page - 1) * page_size
    end = start + page_size

    return (start, end)
