def merge(lst):
    return [[sub[i] for sub in lst] for i in range(2)]

print(merge([['x',  'y'], ['a', 'b'], ['m', 'n']]))  # [['x', 'a', 'm'], ['y', 'b', 'n']]

Explanation:
The function `merge` takes a list of lists as its argument. It uses a list comprehension to create new lists. The outer list comprehension runs twice, representing the two lists that the function should return. The inner list comprehension runs for each sublist in the input list and picks out the i-th element (where i is 0 or 1).
"""

