"""
Explanation:
Given a string of length n, there are n(n+1)/2 non-empty substrings.
We can count the substrings by iterating through each character in the string and finding all substrings starting from that character.
"""

def number_of_substrings(s):
    n = len(s)
    return n*(n+1)//2

# Test cases
assert number_of_substrings("abc") == 6
assert number_of_substrings("abcd") == 10
assert number_of_substrings("abcde") == 15
assert number_of_substrings("abcdef") == 21

print("All tests pass")
<jupyter_output>
All tests pass
<jupyter_text>
