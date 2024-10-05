from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]

# Test cases
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python', 'is', 'awesome'], 'a'))  # []
print(filter_by_prefix(['apple', 'ant', 'axe', 'dog', 'cat', 'bat'], 'a'))  # ['apple', 'ant', 'axe', 'bat']
print(filter_by_prefix(['red', 'green', 'blue', 'orange', 'purple'], 'o'))  # ['orange', 'purple']
print(filter_by_prefix(['snow', 'sun', 'sand', 'sea', 'sky'], 's'))  # ['snow', 'sun', 'sand', 'sea', 'sky']
print(filter_by_prefix(['one', 'two', 'three', 'four', 'five'], 'f'))  # ['four', 'five']
print(filter_by_prefix(['car', 'bus', 'truck', 'van', 'boat'], 'b'))  # ['bus', 'truck', 'van', 'boat']
print(filter_by_prefix(['monday', 'tuesday', 'wednesday', 'thursday', 'friday'], 't'))  # ['tuesday', 'thursday']
print(filter_by_prefix(['apple', 'banana', 'cherry', 'date', 'fig'], 'c'))  # ['cherry']
print(filter_by_prefix(['apple', 'banana', 'cherry', 'date', 'fig'], 'a'))  # ['apple']
print(filter_by_prefix(['apple', 'banana', 'cherry', 'date', 'fig'], 'd'))  # ['date']
print(filter_by_prefix(['apple', 'banana', 'cherry', 'date', 'fig'], 'f'))  # ['fig']
print(