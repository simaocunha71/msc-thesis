from typing import List

def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(1, len(string) + 1):
        prefixes.append(string[:i])
    return prefixes

# Test
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
# Time complexity: O(n)
# Space complexity: O(n) where n is the length of the input string
# The function iterates over the input string once, and creates a list of all prefixes of the input string. Therefore, the time complexity is O(n) and the space complexity is also O(n) because the function creates a list of all prefixes.  # noqa: E501
# Complexity Analysis:
# The time complexity is O(n), where n is the length of the input string.
# The function iterates over the input string once, so the time complexity is O(n).
# The space complexity is O(n), where n is the length of the input string.
# The function creates a list of all prefixes of the input string, so the space complexity is O(n).