def number_of_substrings(s):
    length = len(s)
    return (length * (length + 1)) // 2

assert number_of_substrings("abc") == 6

# The idea here is to calculate the number of substrings of a string of length n.
# This can be done using the formula n*(n+1)/2. So, we find the length of the string,
# then use the formula to calculate the number of substrings.
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 5**
<jupyter_code>
