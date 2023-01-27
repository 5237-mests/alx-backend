#!/usr/bin/python3
"""Module task 2
"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class inherit BaseCaching class"""
    def __init__(self):
        """init class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put data data into dict"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """gets data from dict"""
        return self.cache_data.get(key, None)
