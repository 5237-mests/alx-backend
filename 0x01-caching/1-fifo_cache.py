#!/usr/bin/python3
"""Module task 0
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """class inherit BaseCaching class"""
    def __init__(self):
        """init class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put data data into dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """gets data from dict"""
        return self.cache_data.get(key, None)
