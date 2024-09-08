def number_of_substrings(s):
    n = len(s)
    return n*(n+1)//2

assert number_of_substrings("abc") == 6
"""
Explanation:
The substrings for the string "abc" are: "a", "b", "c", "ab", "bc", "abc". So, the function returns n*(n+1)//2.
"""

