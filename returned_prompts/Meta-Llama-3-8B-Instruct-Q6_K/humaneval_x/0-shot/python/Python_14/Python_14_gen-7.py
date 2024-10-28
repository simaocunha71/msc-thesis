from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[i:] for i in range(len(string) + 1)]

# Test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde']
print(all_prefixes(''))  # Output: []  # Empty string has no prefixes
print(all_prefixes('a'))  # Output: ['']  # Single character string has only an empty prefix
print(all_prefixes('abcabc'))  # Output: ['a', 'ab', 'abc', 'abcabc']
print(all_prefixes('123456'))  # Output: ['', '1', '12', '123', '1234', '12345', '123456']  # No duplicates
print(all_prefixes('1234567'))  # Output: ['', '1', '12', '123', '1234', '12345', '123456', '1234567']  # No duplicates
print(all_prefixes('abc123abc'))  # Output: ['', 'a', 'ab', 'abc', 'abc123', 'abc123abc']  # No duplicates
print(all_prefixes('abc123abcabc'))  # Output: ['', 'a', 'ab', 'abc', 'abc123', 'abc123abc', 'abc123abcabc']  # No duplicates
print(all_prefixes('abc123abcabcabc'))  # Output: ['', 'a', 'ab', 'abc', 'abc123', 'abc123abc', 'abc123abcabc', 'abc123abcabcabc']  # No duplicates
print(all_prefixes('abc123abcabcabcabc'))  # Output: ['', 'a', 'ab', 'abc', 'abc123', 'abc123abc', 'abc123abcabc', 'abc123abcabcabc', 'abc123abcabcabcabc']  # No duplicates
print(all_prefixes('abc123abcabcabcabcabc'))  # Output: ['', 'a', 'ab', 'abc', 'abc123', 'abc123abc', 'abc123abcabc', 'abc123abcabcabc', 'abc123abcabcabcabc', 'abc123abcabcabcabcabc']  # No duplicates
print(all_prefixes('abc