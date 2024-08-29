def merge(lst):
    return [list(x) for x in zip(*lst)]

print(merge([['x',  'y'], ['a',  'b'], ['m',  'n']]))  # should return [['x', 'a', 'm'], ['y', 'b', 'n']]

"""
Explanation:
The function uses the built-in zip function in python which can take two or more iterables (like lists) and returns an iterator that generates tuples containing i-th element from each of the argument sequences. The asterisk (*) is used to unpack the input list.
The list comprehension is used to create the output lists.
"""

#Test case
assert merge([['x',  'y'], ['a',  'b'], ['m',  'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
<jupyter_output>
[['x', 'a', 'm'], ['y', 'b', 'n']]
<jupyter_text>
Question 3
<jupyter_code>
