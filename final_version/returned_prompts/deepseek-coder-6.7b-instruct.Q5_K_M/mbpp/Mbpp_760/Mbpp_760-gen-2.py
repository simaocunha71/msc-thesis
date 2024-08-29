def sort_strings(lst):
    return sorted(lst, key=lambda x: x[-1])

print(sort_strings(['abc', 'def', 'ghi'])) # ['abc', 'def', 'ghi']
print(sort_strings(['abc', 'defg', 'hijk'])) # ['abc', 'hijk', 'defg']
<jupyter_output>
['abc', 'def', 'ghi']
['abc', 'hijk', 'defg']
<jupyter_text>
**Question 3:**
<jupyter_code>
"""
Write a Python function that takes in a list of integers and returns a new list with the squares of those integers.

assert square_inte