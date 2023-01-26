#!/usr/bin/python3
"""Module task 0
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """class inherit BaseCaching class"""
    def put(self, key, item):
        """put data data into dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets data from dict"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
