from typing import List


def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes


# Test
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']
print(all_prefixes('a'))  # Output: ['a']
print(all_prefixes(''))  # Output: []
print(all_prefixes('abcd'))  # Output: ['a', 'ab', 'abc', 'abcd']  # Output: ['a', 'ab', 'abc', 'abcd']
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde']
print(all_prefixes('abcdef'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef']
print(all_prefixes('abcdefg'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg']
print(all_prefixes('abcdefgh'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh']
print(all_prefixes('abcdefghi'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi']
print(all_prefixes('abcdefghij'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij']
print(all_prefixes('abcdefghijk'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk']
print(all_prefixes('abcdefghijkl'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghijk', 'abcdefghijkl']
print(all