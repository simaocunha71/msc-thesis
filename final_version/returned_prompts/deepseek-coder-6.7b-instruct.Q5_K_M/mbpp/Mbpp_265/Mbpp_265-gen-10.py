def list_split(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))

"""
Output:
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
"""

Explanation:
The function uses list comprehension to create a new list. It slices the original list from index i to i+n, incrementing by n at each iteration. It continues this until it has iterated over the entire list. This results in a list of lists, each containing n elements.
"""

# Another way using numpy
import numpy as np

def list_split(l, n):
    return [list(x) for x in np.array_split(l, len(l) // n)]

print(list_split(['a',  'b',  'c',  'd',  'e',  'f',  'g',  'h',  'i',  'j',  'k',  'l',  'm',  'n'],3))

"""
Output:
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n']]
"""

Explanation:
The function uses numpy's array_split method to split the list into n parts. The function then converts each part back into a list before adding it to the final output list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
"""
