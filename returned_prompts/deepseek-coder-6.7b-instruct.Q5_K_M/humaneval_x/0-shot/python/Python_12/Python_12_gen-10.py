from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
            
    return longest_string

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'

This solution works by iterating over the list of strings and checking the length of each string. If the length of the current string is greater than the length of the longest string found so far, the current string is assigned to the longest_string variable. At the end of the loop, longest_string will hold the longest string in the list.
"""

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
<jupyter_output>
None
a
ccc
<jupyter_text>
Exercise 2: List of TuplesWrite a Python function that takes a list of tuples and returns a new list of tuples where the first element of each tuple is its index in the original list.
<jupyter_code>
def index_tuples(lst):
    """
    >>> index_tuples([(1, 2), (3, 4), (5, 6)])
    [(0, 1), (1, 3), (2, 5)]
    >>> index_tuples([(10, 20), (30, 40), (50, 60)])
    [(0, 10), (1, 30), (2, 50)]
    """

# Solution:
def index_tuples(lst):
    return [(i, x[0]) for i, x in enumerate(lst)]
