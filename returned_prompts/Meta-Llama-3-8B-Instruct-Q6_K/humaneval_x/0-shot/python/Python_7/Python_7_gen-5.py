from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # Expected: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'xyz'))  # Expected: []


# Note: The function filter_by_substring takes two parameters: a list of strings and a substring.
# It uses a list comprehension to iterate over the list of strings and includes only those strings that contain the given substring.
# The function returns the filtered list of strings.

# In the test cases, we test the function with different inputs to ensure it works correctly. The expected output for each test case is also provided.
# For example, when we call filter_by_substring([], 'a'), the expected output is an empty list because the input list is empty.
# When we call filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), the expected output is a list containing 'abc', 'bacd', and 'array' because these strings contain the substring 'a'.
# When we call filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'xyz'), the expected output is an empty list because none of the strings in the input list contain the substring 'xyz'.