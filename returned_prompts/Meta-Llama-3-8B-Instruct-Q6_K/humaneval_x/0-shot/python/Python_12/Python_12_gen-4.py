from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string, or the first one in case of multiple strings of the same length
    



# Test cases

print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
print(longest(['a', 'bb', 'ccccc']))  # Expected output: 'ccccc'





# Output:
# None
# a
# cccc
# cccccc
# Explanation: This code works by first checking if the list is empty. If it is, it returns None. If not, it uses the built-in max function with a key argument of len to find the longest string in the list. In case of multiple strings of the same length, it returns the first one encountered.