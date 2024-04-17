#!/usr/bin/python3
class MyList(list):
    """A subclass of list."""
    def print_sorted(self, key=None):
        """Prints the elements of the list in ascending order, sorted by the given key function."""
        print(sorted(self, key=key))
