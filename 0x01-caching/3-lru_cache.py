#!/usr/bin/env python3
"""Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.

        Args:
            key: The key associated with the item.
            item: The item to be added to the cache.

        Returns:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key not in self.usedKeys:
                # Add key to the end of usedKeys
                self.usedKeys.append(key)
            else:
                # Move key to the end of usedKeys
                self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))

            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                # Remove the least recently used item from the cache
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))


    def get(self, key):
        """
        Retrieves an item from the cache
        based on the specified key.

        Args:
            key: The key associated with the
            item to retrieve.

        Returns:
            The item associated with the key,
            or None if the key is not found.
        """
        if key is not None and key in self.cache_data.keys():
            # Move the key to the end of usedKeys
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            return self.cache_data.get(key)
        return None
