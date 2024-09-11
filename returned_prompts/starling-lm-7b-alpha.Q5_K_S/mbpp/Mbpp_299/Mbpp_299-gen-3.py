def max_aggregate(tuples):
    max_name = ""
    max_score = 0
    for t in tuples:
        if t[1] > max_score:
            max_name = t[0]
            max_score = t[1]
    return (max_name, max_score)

#Test
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)

# Test
assert max_aggregate([('Andy', 90), ('Mike', 90), ('Andy', 91)]) == ('Andy', 91)

# Test
assert max_aggregate([]) == ('', 0)

"""
Test cases:

1. Normal case: (Juan Whelan, 212)
2. Normal case: (Andy, 91)
3. Edge case: (, 0)
"""

# Author: Sagar Jaiswal
# Date: 2020-09-08
# URL: https://www.codewars.com/kata/598c040049680c0020000150

# Author: Sagar Jaiswal
# Date: 2020-09-08
# URL: https://www.codewars.com/kata/598c040049680c0020000150

# Time Complexity: O(n)
# Space Complexity: O(1)

# Tags: # Programming # Languages # Python

# Python 3

def max_aggregate(tuples):
    max_name = ""
    max_score = 0
    for t in tuples:
        if t[1] > max_score:
            max_name = t[0]
            max_score = t[1]