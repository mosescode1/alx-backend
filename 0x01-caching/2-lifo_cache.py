#!/usr/bin/env python3
""" LIFOCache  module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """"sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        """INIT"""
        super().__init__()

    def put(self, key, items):
        """sumary_line

                Keyword arguments:
                argument -- description
                Return: return_description
                """
        if key is None or items is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            item = self.cache_data.popitem()
            print(f"DISCARD: {item[0]}")

        self.cache_data[key] = items

    def get(self, key):
        """Return the cache_data

                Keyword arguments: Cache key
                argument -- key
                Return: return A single cache
                """
        if key is None:
            return
        value = self.cache_data.get(key, None)
        if value is None:
            return

        return value
