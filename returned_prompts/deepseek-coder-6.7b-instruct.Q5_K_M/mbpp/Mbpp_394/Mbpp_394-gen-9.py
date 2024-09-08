
def check_distinct(t):
    return len(t) == len(set(t))

assert check_distinct((1, 4, 5, 6, 1, 4)) == False
"""
The function works by first converting the tuple to a set. A set in Python is a data type that contains no duplicate elements. When we convert the tuple to a set, any duplicate elements are automatically removed. Then, we compare the length of the set with the original tuple. If the lengths are equal, this means that the tuple had no duplicate elements, and we return True. Otherwise, we return False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 2**
<jupyter_code>
