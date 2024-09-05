#!/usr/bin/env python3
"""Small BaseCaching module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''Caching system
    '''

    def __init__(self):
        """ Initiliaze
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''Add an item in the cache
        '''
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        '''Get an item by key
        '''
        if key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
