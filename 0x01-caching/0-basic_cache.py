#!/usr/bin/env python3
"""
    This script downloads the raw images from Flickr and puts them in folders
"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """
        Basic caching mechanism.
    """

    def put(self, key, item):
        """
            Puts item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
            Get item from the cache
        """
        return self.cache_data.get(key, None)