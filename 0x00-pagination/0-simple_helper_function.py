#!/usr/bin/env python3
"""0-simple_helper_function"""


def index_range(page, page_size):
    """function return a tuple of size two containing a
    start index and an end index of page"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
