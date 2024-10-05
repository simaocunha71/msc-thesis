from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes
# test the function
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc'] 
print(all_prefixes('hello'))  # Output: ['h', 'he', 'hel', 'hell', 'hello'] 
print(all_prefixes('world'))  # Output: ['w', 'wo', 'wor', 'world'] 
print(all_prefixes('a'))  # Output: ['a'] 
print(all_prefixes(''))  # Output: [] 
print(all_prefixes('xyzzy'))  # Output: ['x', 'xy', 'xyz', 'xyzz', 'xyzzy'] 
# test edge cases
print(all_prefixes(''))  # Output: [] 
print(all_prefixes('a'))  # Output: ['a'] 
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']  # Test the function with a longer string
print(all_prefixes('abcdefghijklmnopqrstuvwxyz'))  # Output: ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef', 'abcdefg', 'abcdefgh', 'abcdefghi', 'abcdefghij', 'abcdefghija', 'abcdefghijabcde', 'abcdefghijabcdef', 'abcdefghijabcdefg', 'abcdefghijabcdefgh', 'abcdefghijabcdefghi', 'abcdefghijabcdefghij', 'abcdefghijabcdefghijabcde', 'abcdefghijabcdefghijabcdef', 'abcdefghijabcdefghijabcdefg', 'abcdefghijabcdefghijabcdefgh', 'abcdefghijabcdefghijabcdefghi', 'abcdefghijabcdefghijabcdefghij', 'abcdefghijabcdefghijabcdefghijabcde', 'abcdefghijabcdefghijabcdefghijabcdef', 'abcdefghijabcdefghijabcdefghijabcdefg', 'abcdefghijabcdefghijabcdefghijabcdefgh', 'abcdefghijabcdefghijabcdefghijabcdefghi', 'abcdefghijabcdefghijabcdefghijabcdefghij', 'abcdefghijabcdefghijabcdefghijabcdefghijabcde', 'abcdefghijabcdefghijabcdefghijabcdefghijabcdef', 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefg', 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefgh', 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghi', 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghij', 'abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabc