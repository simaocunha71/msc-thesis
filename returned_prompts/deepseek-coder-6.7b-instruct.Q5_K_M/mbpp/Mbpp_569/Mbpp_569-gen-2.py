def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))

"""
Output:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

In this code, we use a list comprehension to iterate over each sublist in the input list. The sorted function is used to sort each sublist. The result is a new list where each sublist is sorted in lexicographic order.

The sorted function returns a new sorted list from the elements of any iterable. It does not sort the elements of the original iterable. The sort is not in-place, i.e., a new list is created instead of modifying the original.
"""


"""
