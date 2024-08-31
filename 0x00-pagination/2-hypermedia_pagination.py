#!/usr/bin/env python3
"""
2-hypermedia_pagination
"""


import csv
from typing import List, Tuple, Dict, Any
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function return a tuple of size two containing a
    start index and an end index of page"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the appropriate page of the dataset."""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert (
            isinstance(page_size, int) and page_size > 0
        ), "Page size must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        end_index = min(end_index, len(dataset))

        return dataset[start_index:end_index] if start_index < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Returns a dictionary"""
        total_page = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page + 1 < total_page else None,
            "prev_page": page - 1 if page - 1 > 0 else None,
            "total_pages": total_page,
        }
