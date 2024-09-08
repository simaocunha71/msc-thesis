def substract_elements(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Both tuples must have the same length.")
    return tuple(a - b for a, b in zip(t1, t2))

print(substract_elements((10, 4, 5), (2, 5, 18)))  # Output: (8, -1, -13)


# Alternative solution using a for loop:
def substract_elements(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Both tuples must have the same length.")
    res = []
    for i in range(len(t1)):
        res.append(t1[i] - t2[i])
    return tuple(res)

print(substract_elements((10, 4, 5), (2, 5, 18)))  # Output: (8, -1, -13)

"""
Explanation:

The function `substract_elements` takes two tuples `t1` and `t2`. It checks if the two tuples have the same length. If not, it raises a `ValueError`. Then, it uses a list comprehension to subtract the corresponding elements of `t2` from `t1` and returns a new tuple.

Alternatively, the function can also be implemented using a for loop. It initializes an empty list `res`, then it iterates over the indices of `t1` and `t2`, subtracts the element at index `i` in `t2` from the element at index `i` in `t1`, and appends the result to `res`. Finally, it returns a new tuple created from `res`.
"""
<jupyter_output>
(8, -1, -13)
(8, -1, -13)
<jupyter_text>
Q2:
<jupyter_code>
"""
Write a function that takes a list of tuples and returns a new list with only the tuples that have a