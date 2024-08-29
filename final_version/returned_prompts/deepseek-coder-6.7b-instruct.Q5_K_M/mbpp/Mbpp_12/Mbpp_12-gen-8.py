def sort_matrix(matrix):
    sum_rows = [sum(row) for row in matrix]
    return [row for _, row in sorted(zip(sum_rows, matrix))]


assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
"""
Explanation:
The function first calculates the sum of each row in the matrix using the built-in sum function. The result of this is a list sum_rows where the i-th element corresponds to the sum of the i-th row in the original matrix.

Then it creates a new list that contains the rows of the original matrix, sorted in ascending order based on the corresponding element of sum_rows. This is done using the built-in sorted function and the zip function.

Finally, the function returns the sorted list of rows.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
