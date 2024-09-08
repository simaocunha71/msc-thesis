
def odd_position(lst):
    return all(i % 2 != 0 for i in lst[::2])

print(odd_position([2,1,4,3,6,7,6,3]))  # Output: True

Explanation:
The function `odd_position` takes a list `lst` as its argument. It checks every second element of the list (indexes are 0, 2, 4, etc.) to see if it is odd (i.e., if `i % 2 != 0`). The `all` function returns `True` if all elements in the iterable (the generator expression here) are `True`. If any are not `True`, `all` returns `False`.

The `[::2]` slice syntax means "start at the beginning of the list, end at the end, and step by 2". So it generates every second element of the list.
"""

#