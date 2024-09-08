"""
The function max_of_nth gets the n'th column of the matrix by using a list comprehension and then returns the max value in this column.
"""

def max_of_nth(matrix, n):
    column = [row[n] for row in matrix]
    return max(column)

# Test
print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)) # Should return 19

