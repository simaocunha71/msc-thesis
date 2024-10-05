from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
    # or using list comprehension
    # return [s for s in strings if s.startswith(prefix)]


Explanation:
The function `filter_by_prefix` takes two parameters: a list of strings `strings` and a prefix `prefix`. It returns a new list containing only the strings from the input list that start with the given prefix.

The function uses a list comprehension to achieve this. The comprehension iterates over each string `s` in the input list `strings`. For each string, it checks if the string starts with the given prefix using the `startswith` method. If it does, the string is included in the new list.

The function can be tested with the following examples:
```
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```


This function is efficient because it uses a list comprehension, which is a built-in Python feature that creates a new list by iterating over an existing iterable. This is faster and more memory-efficient than creating a new list by appending elements one by one using a for loop. The `startswith` method is also an O(1) operation, so the time complexity of the function is O(n), where n is the length of the input list. The space complexity is also O(n), because the function creates a new list that can be as large as the input list.