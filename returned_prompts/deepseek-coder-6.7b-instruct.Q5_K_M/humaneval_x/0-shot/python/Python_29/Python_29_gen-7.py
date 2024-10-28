from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']


This solution uses Python's list comprehension to filter the strings. For each string in the list, it checks if the string starts with the given prefix using the built-in `startswith` function. If the string starts with the prefix, it is included in the resulting list. Otherwise, it is not included.

This solution has a time complexity of O(n), where n is the number of strings in the list. This is because it needs to go through each string in the list once. The space complexity is also O(n), where n is the number of strings that start with the given prefix. This is because it creates a new list that contains all the strings that start with the given prefix.

In terms of code readability, this solution is quite straightforward and easy to understand. It uses Python's built-in functions and features in a very pythonic way.
"""

# 2.
"""
