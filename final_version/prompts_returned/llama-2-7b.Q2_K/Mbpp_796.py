"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
from typing import Optional
def return_sum(dictionary: dict) -> int:
    """Define function to find the sum of all items in a dictionary.
    Note that dictionaries are unordered (the order is not important), so if you want to order them, you should pass a list with your dictionary."""

    total = 0

    for key, value in dictionary.items():
        total += int(value)

    return total