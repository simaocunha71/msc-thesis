from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], ''))  # Expected output: ['abc', 'bcd', 'cde', 'array']  # All strings start with an empty prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'bc'))  # Expected output: ['bcd']  # Only one string starts with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'cd'))  # Expected output: ['cde']  # Only one string starts with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'array'))  # Expected output: ['array']  # Only one string starts with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'xyz'))  # Expected output: []  # No strings start with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'de'))  # Expected output: []  # No strings start with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'bcde'))  # Expected output: ['bcde']  # Only one string starts with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'abcde'))  # Expected output: ['abcde']  # Only one string starts with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'abcd'))  # Expected output: ['abcd']  # Only one string starts with the given prefix
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'abcde'))  # Expected output: ['abcde']  # Only one string starts with the given prefix
print(filter