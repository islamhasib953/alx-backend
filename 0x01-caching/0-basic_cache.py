#!/usr/bin/python3
""" 0-basic_cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Class BasicCache"""

    def __init__(self):
        """init class!"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary"""
        if key and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value"""
        if key is None or key not in self.cache_data.keys():
            return None
        return "{}: {}".format(key, self.cache_data.get(key))
