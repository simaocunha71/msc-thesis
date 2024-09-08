
def union_elements(t1, t2):
    return tuple(sorted(set(t1 + t2)))

print(union_elements((3, 4, 5, 6),(5, 7, 4, 10)))
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) )== (3, 4, 5, 6, 7, 10)
"""
This function works by first concatenating the two input tuples using the '+' operator. This results in a new tuple that contains all the elements of both input tuples.
Then, the set function is used to remove duplicate elements from the new tuple. The sorted function is used to sort the resulting tuple in ascending order before it is returned by the function.
"""

"""
