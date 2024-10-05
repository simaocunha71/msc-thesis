from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test cases
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']  # Test case 2
print(filter_by_prefix(['x', 'y', 'z'], 'a'))  # Expected output: []  # Test case 3
print(filter_by_prefix(['a', 'b', 'c'], 'd'))  # Expected output: []  # Test case 4
print(filter_by_prefix(['a', 'b', 'c'], 'a'))  # Expected output: ['a']  # Test case 5
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc'))  # Expected output: ['abc', 'abcd', 'abcde']  # Test case 6
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'def'))  # Expected output: []  # Test case 7
print(filter_by_prefix([], ''))  # Expected output: []  # Test case 8
print(filter_by_prefix(['abc', 'abcd', 'abcde'], ''))  # Expected output: ['abc', 'abcd', 'abcde']  # Test case 9
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc'))  # Expected output: ['abc', 'abcd', 'abcde']  # Test case 10
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abcdef'))  # Expected output: []  # Test case 11
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abcde'))  # Expected output: ['abcde']  # Test case 12
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abcde'))  # Expected output: ['abcde']  # Test case 13
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abcde'))  # Expected output: ['abcde']  # Test case 14
print(filter_by_prefix(['abc', 'abcd', 'abcde'], 'abcde'))  # Expected output: ['abcde']  # Test case 15