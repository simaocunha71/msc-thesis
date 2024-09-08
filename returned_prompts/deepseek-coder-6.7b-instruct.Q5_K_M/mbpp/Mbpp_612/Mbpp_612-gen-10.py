def merge(lst):
    return [[i[j] for i in lst] for j in range(2)]

print(merge([['x',  'y'], ['a', 'b'], ['m', 'n']]))

"""
Explanation:
The function `merge` takes a list of lists `lst` as an argument. It returns a list of two lists.

For each index `j` in the range `0, 1` (which is equivalent to `2` in this context, as Python ranges are exclusive of the stop index), it creates a new list that contains the `j`th element of each sublist in `lst`.

So for the first index `j` (which is `0`), it creates a list that contains the first element of each sublist (`'x'`, `'a'`, and `'m'`), and for the second index `j` (which is `1`), it creates a list that contains the second element of each sublist (`'y'`, `'b'`, and `'n'`).

Finally, it returns a list containing the two newly created lists.
"""

#  OUTPUT: 
# [['x', 'a', 'm'], ['y', 'b', 'n']]
<jupyter_output>
[['x', 'a', 'm'], ['y', 'b', 'n']]
<jupyter_text>
Question 2:
<jupyter_code>
