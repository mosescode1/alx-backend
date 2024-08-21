#!/usr/bin/env python3
""" MRUCache  module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """"sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        """INIT"""
        super().__init__()
        self.current = None

    def put(self, key, items):
        """sumary_line

                Keyword arguments:
                argument -- description
                Return: return_description
                """
        if key is None or items is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = items
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.current)
            print(f"DISCARD: {self.current}")

        self.current = key
        self.cache_data[key] = items

    def get(self, key):
        """Return the cache_data

                Keyword arguments: Cache key
                argument -- key
                Return: return A single cache
                """
        if key is None:
            return

        if key in self.cache_data:
            self.current = key
            return self.cache_data[key]

        return None
