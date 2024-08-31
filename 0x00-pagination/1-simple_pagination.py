#!/usr/bin/env python3
"""
1-simple_pagination
"""


import csv
from typing import List, Tuple


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
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        end_index = min(end_index, len(dataset))

        return dataset[start_index:end_index] if start_index < len(dataset) else []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing a start and end index."""
    return ((page - 1) * page_size, page * page_size)
