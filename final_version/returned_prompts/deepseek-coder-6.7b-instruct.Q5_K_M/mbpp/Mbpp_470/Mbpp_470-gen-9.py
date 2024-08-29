def add_pairwise(t):
    return tuple(t[i+1]+t[i] for i in range(len(t)-1))

print(add_pairwise((1, 5, 7, 8, 10)))

#Output
(6, 12, 15, 18)

#Explanation
The function add_pairwise takes a tuple t as input. It then uses a tuple comprehension to iterate over the indices of the tuple from 0 up to len(t)-1. For each index i, it adds the element at index i+1 to the element at index i and returns this result as part of a new tuple.
"""

#Solution 2:
