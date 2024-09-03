#!/usr/bin/python3
""""4-mru_cache"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Class LFUCache"""

    def __init__(self):
        """init class"""
        super().__init__()
        self.queue = []
        self.add = 0

    def put(self, key, item):
        """assign to the dictionary"""
        if key and item is not None:
            if (
                len(self.cache_data) >= BaseCaching.MAX_ITEMS
                and key not in self.cache_data
            ):
                self.queue.sort()
                print("DISCARD: {}".format(self.queue[0][1]))
                del self.cache_data[self.queue[0][1]]
                del self.queue[0]
            if key in self.queue:
                self.add = 1 + self.queue[0][key]
            self.queue.append((self.add, key))
            self.cache_data[key] = item
            self.add = 0

    def get(self, key):
        """return the value"""
        if key is None or key not in self.cache_data.keys():
            return None
        # del self.queue[self.queue.index(key)]
        # self.queue.append(key)
        return self.cache_data.get(key)
