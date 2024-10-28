from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # ['hello', 'world']
print(filter_by_substring(['hello', 'world', 'python'], 'z'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'xyz'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], ''))  # ['abc', 'bacd', 'cde', 'array']  # empty string matches any string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'abc'))  # ['abc', 'bacd', 'array']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'bac'))  # ['bacd']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'array'))  # ['array']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'd'))  # ['bacd']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'e'))  # ['cde']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'c'))  # ['cde']  # matches if substring is in string
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'python'))  # []  # matches if substring is in string
print(filter_by_substring(['abc