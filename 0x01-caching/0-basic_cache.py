#!/usr/bin/env python3
""" BaseCaching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
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
        if key == None or items == None:
            return
        self.cache_data[key] = items

    def get(self, key):
        """Return the cache_data

                Keyword arguments: Cache key
                argument -- key
                Return: return A single cache
                """
        if key == None:
            return
        value = self.cache_data.get(key)
        if value is None:
            return

        return value
