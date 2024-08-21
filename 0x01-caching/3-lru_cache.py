#!/usr/bin/env python3
""" LRUCache  module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """"sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        """INIT"""
        super().__init__()
        self.current = []

    def put(self, key, items):
        """sumary_line

                Keyword arguments:
                argument -- description
                Return: return_description
                """
        if key is None or items is None:
            return

        if key in self.cache_data:
            self.current.remove(key)

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.current.pop()
            self.cache_data.pop(lru)
            print(f"DISCARD: {lru}")

        self.current.insert(0, key)
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

        if value is not None:
            self.current.remove(key)
            self.current.insert(0, key)

        return value
