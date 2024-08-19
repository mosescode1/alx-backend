#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0,
                        page_size: int = 10) -> Dict:
        """
        Returns a dictionary with the following key-value pairs:
        - 'index': the current start index of the return page
        - 'next_index': the start index of the next page
        - 'page_size': the size of the current page
        - 'data': the actual page data
        """
        indexed_data = self.indexed_dataset()
        assert index < len(self.__dataset)
        data = []
        next_index = index

        while len(data) < page_size and next_index < len(indexed_data):
            item = indexed_data.get(next_index)
            if item:
                data.append(item)
            next_index += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
