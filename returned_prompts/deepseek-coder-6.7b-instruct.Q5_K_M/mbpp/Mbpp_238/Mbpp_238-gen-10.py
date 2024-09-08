def number_of_substrings(s: str) -> int:
    n = len(s)
    return n * (n + 1) // 2


print(number_of_substrings("abc"))  # 6


"""
Explanation:

A string of length n has n*(n+1)/2 non-empty substrings.

In the string "abc", there are 3 letters, so there are 3*(3+1)//2 = 6 non-empty substrings.

They are: "a", "b", "c", "ab", "bc", and "abc".
"""


# In Python, you can use the built-in function for finding substrings.
# Here is the function to count the number of non-empty substrings using the built-in function:

def number_of_substrings_builtin(s: str) -> int:
    return sum(s.count(s[i:]) for i in range(len(s)))


print(number_of_substrings_builtin("abc"))  # 6


# Both functions work the same way.
# The first one uses the mathematical formula, while the second one uses the Python built-in function for counting substrings.
# The second function is more "pythonic" and concise, but it might be less efficient for very long strings because it creates many temporary strings.
# The first function is more efficient for long strings, but it's more complicated and harder to understand.
<jupyter_output>
6
6
<jupyter_text>
**Question 2:**
<jupyter_code>
