from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if not strings:  # Check if the list is empty
        return None

    longest_str = max(strings, key=len)  # Use the max function with a key function to find the longest string
    return longest_str
    



# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'







# Additional test cases
print(longest(['abc', 'abcd', 'abcde']))  # Expected output: 'abcde'
print(longest(['a', 'b', 'c', 'd', 'e']))  # Expected output: 'e'
print(longest(['hello', 'world', 'python']))  # Expected output: 'python'

# Edge cases
print(longest(['']))  # Expected output: ''
print(longest(['a']))  # Expected output: 'a'
print(longest(['a', 'a']))  # Expected output: 'a'







# Test case for duplicate longest strings
print(longest(['a', 'abc', 'abc']))  # Expected output: 'abc'







# Test case for strings with different lengths
print(longest(['abc', 'def', 'ghi', 'jkl', 'mno']))  # Expected output: 'mno'







# Test case for strings with same length
print(longest(['abc', 'def', 'ghi', 'jkl']))  # Expected output: 'jkl'







# Test case for strings with different lengths
print(longest(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']))  # Expected output: 'pqr'







# Test case for strings with same length
print(longest(['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']))  # Expected output: 'pqr'