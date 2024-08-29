def sort_matrix(matrix):
    return [row for row in sorted(matrix, key=sum)]

assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""
This function works by using the built-in sorted function in Python, which sorts the rows of the matrix in ascending order according to the sum of their elements. It does this by providing the key argument as sum, which tells Python to use the sum of the elements as the sorting key.
"""

#Solution2:
def sort_matrix(matrix):
    return sorted(matrix, key=sum)

assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""
This solution is essentially the same as the first one, but it doesn't use a list comprehension to create a new list. Instead, it directly returns the sorted matrix.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
