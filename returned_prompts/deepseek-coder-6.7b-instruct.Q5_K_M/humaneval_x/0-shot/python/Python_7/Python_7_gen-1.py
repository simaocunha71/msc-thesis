from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))

# ['abc', 'bacd', 'array']

print(filter_by_substring([], 'a'))
# []

This function uses a list comprehension to create a new list that only contains the strings that contain the provided substring. The "in" operator is used to check if the substring is in the string.

The time complexity of this function is O(n*m), where n is the number of strings and m is the length of the longest string. This is because for each string, we may have to check every character.
The space complexity is O(k), where k is the number of strings that contain the substring, as we create a new list to store these strings.
"""

# 11.11

"""
