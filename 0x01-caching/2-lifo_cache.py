#!/usr/bin/env python3
"""
 a class LIFOCache that inherits from
 BaseCaching and is a caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
          Adds or updates an item in the cache with the
          given key and value.

            Args:
                key: The key to associate the item with.
                item: The item to be added or updated in the cache.

            Returns:
                None
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """
            Retrieves the item associated with the given
                key from the cache.

            Args:
                key: The key for which to retrieve the item.

            Returns:
                The item associated with the key, or None
                if the key is not present in the cache.
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)