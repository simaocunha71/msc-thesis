from typing import List

def all_prefixes(string: str) -> List[str]:
    return [string[:i+1] for i in range(len(string))]
# test the function
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
print(all_prefixes('abcd'))  # ['a', 'ab', 'abc', 'abcd']
print(all_prefixes(''))  # []


def all_suffixes(string: str) -> List[str]:
    return [string[i+1:] for i in range(len(string))]
# test the function
print(all_suffixes('abc'))  # ['bc', 'c']
print(all_suffixes('abcd'))  # ['bcd', 'cd']
print(all_suffixes(''))  # []


def all_substrings(string: str) -> List[str]:
    return [string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]
# test the function
print(all_substrings('abc'))  # ['a', 'ab', 'abc', 'b', 'bc', 'c']
print(all_substrings('abcd'))  # ['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'bcd', 'c', 'cd', 'd']
print(all_substrings(''))  # []
print(all_substrings('a'))  # ['a']
print(all_substrings('ab'))  # ['a', 'ab']






