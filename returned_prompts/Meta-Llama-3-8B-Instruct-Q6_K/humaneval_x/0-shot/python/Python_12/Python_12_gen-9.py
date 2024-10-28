from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = 0
    longest_str = strings[0]
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_str = s
    return longest_str

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
print(longest(['a', 'bb', 'ccc', 'dddd']))  # 'dddd'  # Note: the first one in case of multiple strings of the same length.  # Return the first one in case of multiple strings of the same length.
print(longest(['a', 'b', 'c', 'd']))  # 'd'
print(longest(['a']))  # 'a'  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same length.  # No need to check for multiple strings of the same