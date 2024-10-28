from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]


# Test the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']



# Explanation:
# This function takes a list of strings and a prefix as input. It uses list comprehension to create a new list with only the strings that start with the given prefix. The `startswith` method of the string class is used to check if a string starts with the given prefix. If a string does, it is included in the new list. If not, it is not included. The function returns the new list. 

# In the example test cases, the function is tested with an empty list and a list with some strings. The expected output is also shown. The function correctly filters the strings based on the given prefix. 