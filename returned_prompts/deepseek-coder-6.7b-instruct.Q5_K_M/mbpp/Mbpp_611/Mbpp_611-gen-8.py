def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
<jupyter_output>
19
<jupyter_text>
3. Write a function that returns the sum of all the numbers in a matrix.
<jupyter_code>
def sum_of_matrix(matrix):
    return sum(sum(row) for row in matrix)

print(sum_of_matrix([[5, 6, 7], [1, 3, 5], [8, 9, 19]]))
<jupyter_output>
66
<jupyter_text>
4. Write a function that rotates a matrix 90 degrees to the right.
<jupyter_code>
def rotate_matrix(matrix):
    return [list(reversed(column)) for column in zip(*matrix)]

print(rotate_matrix([[5, 6, 7], [1, 3, 5], [8, 9, 19]]))
<jupyter_output>
[[7, 5, 8], [6, 3, 9], [5, 1, 19]]
<jupyter_text>
5. Given a list of lists (matrix), write a function that returns a new matrix where each element is the product of the corresponding elements in the original matrix.
<jupyter_code>
def multiply_matrix(matrix):
    return [[element*2 for element in row] for row in matrix]

print(multiply_matrix([[5, 6, 7], [1, 3, 5], [8, 9, 19]]))
<jupyter_output>
[[10, 12, 14], [2, 6, 10], [16, 18, 38]]
<jupyter_text>
6. Write a function that given a matrix