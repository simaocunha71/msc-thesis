def tuple_modulo(t1, t2):
    return tuple(i % j for i, j in zip(t1, t2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))

# Output: (0, 4, 5, 1)

"""
Explanation:
The function tuple_modulo takes two tuples t1 and t2 of the same length as input. The zip function is used to pair elements from t1 and t2 at the same index. For each pair (i, j), the modulo operation is performed and the result is collected in a new tuple which is returned by the function.
"""

# Question 3

