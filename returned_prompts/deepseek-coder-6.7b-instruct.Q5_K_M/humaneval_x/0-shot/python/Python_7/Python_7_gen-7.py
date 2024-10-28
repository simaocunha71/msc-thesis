from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]


print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']


