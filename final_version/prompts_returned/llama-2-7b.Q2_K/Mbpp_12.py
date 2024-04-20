"""
Write a function to sort a given matrix in ascending order according to the sum of its rows.
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""

def sum_of_rows(matrix):
    """Sum up the number of rows in a matrix."""

    # Add one if the size is odd. (Odd because we're only
    # counting the numbers, not including the '1' on its own)
    mat = [[0] + [1] * len(matrix[0]) for i in range(len(matrix))]
    
    # Add up each row
    for row in zip(*matrix):
        sum_of_rows += 1 if (row == '1') else 0
    mat.sort()
    return mat


print(sum_of_rows([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))