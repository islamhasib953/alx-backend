#!/usr/bin/python3
""""4-mru_cache"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Class MRUCache"""

    def __init__(self):
        """init class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assign to the dictionary"""
        if key and item is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data
            ):
                print("DISCARD: {}".format(self.queue[-1]))
                del self.cache_data[self.queue[-1]]
                del self.queue[-1]
            if key in self.queue:
                del self.queue[self.queue.index(key)]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """return the value"""
        if key is None or key not in self.cache_data.keys():
            return None
        del self.queue[self.queue.index(key)]
        self.queue.append(key)
        return self.cache_data.get(key)
