def max_of_nth(matrix, n):
    if isinstance(matrix, list) and all(isinstance(i, list) for i in matrix):
        if isinstance(n, int) and n >= 0:
            return max([row[n] for row in matrix])
    raise ValueError("Incorrect input format")

# Test
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19

# Test with incorrect input
try:
    max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 8)
    raise ValueError("Should have raised error with incorrect n")
except ValueError:
    pass

try:
    max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], "a")
    raise ValueError("Should have raised error with incorrect n")
except ValueError:
    pass

try:
    max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], -1)
    raise ValueError("Should have raised error with incorrect n")
except ValueError:
    pass

try:
    max_of_nth(["a", "b", "c"], 0)
    raise ValueError("Should have raised error with incorrect matrix")
except ValueError:
    pass

try:
    max_of_nth([5, 6, 7, 8, 9], 2)
    raise ValueError("Should have raised error with incorrect matrix")
except ValueError:
    pass

print("All tests passed")

# END QUESTION

"""
Here's a Python function that takes a matrix and an integer as input and returns the maximum value in the nth column of the matrix:

The function first checks if the input is a list and if all elements in the list are also lists. This ensures that the input is a valid matrix.

Next, the function checks if the input integer is non-negative