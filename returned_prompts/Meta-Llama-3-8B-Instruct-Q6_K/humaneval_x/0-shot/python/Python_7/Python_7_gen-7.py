from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']



Note: The provided function `filter_by_substring` takes a list of strings and a substring as inputs, and returns a new list containing only the strings from the input list that contain the given substring. The function uses a list comprehension to achieve this.

Example usage:
- `filter_by_substring([], 'a')` returns an empty list because there are no strings in the input list that contain the substring 'a'.
- `filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')` returns a list containing 'abc', 'bacd', and 'array' because these strings contain the substring 'a'. The string 'cde' is not included in the output list because it does not contain the substring 'a'.