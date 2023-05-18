#!/usr/bin/env python3
""" 
a class LFUCache that inherits from
BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Least Frequently Used (LFU) Cache implementation.
    This class inherits from the BaseCaching class.
    """

    def __init__(self) -> None:
        """
        Initializes an instance of the LFUCache class.
        """
        self.temp_list = {}  
        # Stores the frequency count for each key
        super().__init__()

    def put(self, key, item):
        """
        Inserts an item into the cache with the specified key.

        Args:
            key: The key associated with the item.
            item: The item to be inserted.
        """
        if not (key is None or item is None):
            # Insert the item into the cache data dictionary
            self.cache_data[key] = item

            # Evict the least frequently used item if the cache is full
            if len(self.cache_data.keys()) > self.MAX_ITEMS:
                # Find the key with the minimum frequency count
                pop = min(self.temp_list, key=self.temp_list.get)
                
                ''' Remove the least frequently used item from
                the cache data and frequency count
                '''
                self.temp_list.pop(pop)
                self.cache_data.pop(pop)
                print(f"DISCARD: {pop}")

            # Update the frequency count for the inserted key
            if not (key in self.temp_list):
                self.temp_list[key] = 0
            else:
                self.temp_list[key] += 1

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
        if (key is None) or not (key in self.cache_data):
            return None

        # Increment the frequency count for the accessed key
        self.temp_list[key] += 1

        # Retrieve and return the item associated with the key
        return self.cache_data.get(key)
