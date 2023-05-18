#!/usr/bin/env python3
"""
a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """_summary_
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Adds or updates an item in the cache with
        the given key and value.

        Args:
            key: The key to associate the item with.
            item: The item to be added or updated in the cache.

        Returns:
            None
        """
        
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with the
        given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key,
            or None if the key is not found in the cache.
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None