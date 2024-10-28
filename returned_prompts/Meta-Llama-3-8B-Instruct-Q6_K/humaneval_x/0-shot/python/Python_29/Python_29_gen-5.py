from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix."""
    return [s for s in strings if s.startswith(prefix)]


# Testing the function
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']



