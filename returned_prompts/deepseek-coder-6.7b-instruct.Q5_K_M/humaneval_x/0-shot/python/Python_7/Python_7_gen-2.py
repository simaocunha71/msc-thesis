from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]


print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']


In this solution, we use a list comprehension to iterate over the input list of strings. We check if the substring is in each string and if it is, we add it to the new list. This solution is efficient because it uses the in operator, which is an O(n) operation where n is the length of the string. This is the best time complexity we can achieve for this problem.
"""
