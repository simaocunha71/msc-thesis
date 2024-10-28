from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[:i] for i in range(1, len(string) + 1)]


# Test
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('abcd'))  # Output: ['a', 'ab', 'abc', 'abcd']
print(all_prefixes(''))  # Output: []
print(all_prefixes('a'))  # Output: ['a']
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde']



