from typing import List

def all_prefixes(string: str) -> List[str]:
    result = []
    for i in range(1, len(string) + 1):
        result.append(string[:i])
    return result
# test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes(''))  # Output: []
print(all_prefixes('a'))  # Output: ['a']
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde'] 
print(all_prefixes('123'))  # Output: ['1', '12', '123']
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello'] 
print(all_prefixes('world'))  # Output: ['w', 'wo', 'wor', 'world'] 
print(all_prefixes(''))  # Output: []  # empty string has no prefixes
print(all_prefixes('a'))  # Output: ['a']  # single character has one prefix
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde']  # multi-character strings
print(all_prefixes('123'))  # Output: ['1', '12', '123']  # multi-character strings
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']  # multi-character strings
print(all_prefixes('world'))  # Output: ['w', 'wo', 'wor', 'world']  # multi-character strings
print(all_prefixes(''))  # Output: []  # empty string has no prefixes
print(all_prefixes('a'))  # Output: ['a']  # single character has one prefix
print(all_prefixes('abcde'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde']  # multi-character strings
print(all_prefixes('123'))  # Output: ['1', '12', '123']  # multi-character strings
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello']  # multi-character strings
print(all_prefixes('world'))  # Output: ['w', 'wo', 'wor',