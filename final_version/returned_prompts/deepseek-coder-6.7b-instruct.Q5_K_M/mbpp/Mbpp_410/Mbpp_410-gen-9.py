def min_val(lst):
    return min(i for i in lst if isinstance(i, int))

print(min_val(['Python', 3, 2, 4, 5, 'version']))

Explanation:
The function min_val takes a list as input. It uses a generator to iterate over the elements of the list, and only includes those elements that are integers in the min() function. The min() function then returns the smallest integer in the list.

"""
Output:
2
"""

"""

