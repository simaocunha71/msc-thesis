from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)


print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'


Explanation:
In Python, the 'join()' method is a string method and returns a string in which the elements of sequence have been joined by str separator. So, in the function 'concatenate', we are using the 'join()' method to concatenate the list of strings into a single string.


This solution has a time complexity of O(n) because it goes through the list of strings once to concatenate them.
"""

# Exercise 3:
"""
