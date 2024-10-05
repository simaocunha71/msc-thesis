from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]

#Testing
print(filter_by_prefix([], 'a')) #Expected: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')) #Expected: ['abc', 'array']

#Python/Programming/Python_Practice/12_Advanced_Python/02_List_Comprehension.py
