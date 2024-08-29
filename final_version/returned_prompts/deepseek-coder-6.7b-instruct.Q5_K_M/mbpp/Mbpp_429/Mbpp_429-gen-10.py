def and_tuples(t1, t2):
    return tuple(x & y for x, y in zip(t1, t2))

print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)))

# Output: (0, 0, 2, 1)

"""
Explanation:
The function `and_tuples` uses the built-in `zip` function to pair elements from the two input tuples together. 
The `zip` function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
The `tuple` function is used to convert the result of the generator expression back into a tuple.
The `&` operator is used to perform the bitwise AND operation on each pair of elements from the input tuples.
"""

# 2
