#!/usr/bin/python3
"""1-fifo_cache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Class FIFOCache"""

    def __init__(self):
        """init class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary"""
        if key and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            discard_key = next(iter(self.cache_data))
            self.cache_data.pop(discard_key)
            print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """return the value"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
