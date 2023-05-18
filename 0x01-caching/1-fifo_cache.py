#!/usr/bin/env python3
"""
a class FIFOCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
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
        
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
                del self.cache_data[item_discarded]
                print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

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
        if key in self.cache_data:
            return self.cache_data[key]
        return None
