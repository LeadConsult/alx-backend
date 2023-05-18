#!/usr/bin/env python3
"""Create a class MRUCache that inherits
from BaseCaching and is a caching system:
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.usedKeys = []

    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.

        Args:
            key: The key associated with the item.
            item: The item to be added to the cache.

        """
        if key is not None and item is not None:
            # Add the item to the cache data dictionary
            self.cache_data[key] = item
            
            # Check if the key is already in usedKeys list
            if key not in self.usedKeys:
                # Append the key to the usedKeys list
                self.usedKeys.append(key)
            else:
                # Move the key to the end of usedKeys list
                self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))

            # Check if the usedKeys list exceeds the maximum limit
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                # Get the second-to-last key from usedKeys list
                discard = self.usedKeys.pop(-2)
                # Remove the corresponding item from cache_data dictionary
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))


    def get(self, key):
        """
        Retrieves the item from the cache associated
        with the specified key.

        Args:
            key: The key associated with the item.

        Returns:
            The item associated with the key,
            or None if the key is not found.

        """
        if key is not None and key in self.cache_data.keys():
            # Move the key to the end of usedKeys list
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
            # Retrieve and return the item associated with the key
            return self.cache_data.get(key)
        # Return None if the key is not found or is None
        return None
