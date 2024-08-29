def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
"""
Explanation:
The function max_of_nth iterates over each row in the matrix and returns the nth element of the row. The built-in max function then returns the largest of these values.
"""

