def magic_square_test(matrix):
    # your code goes here
    sum_row = [sum(row) for row in matrix]
    sum_col = [sum(column) for column in zip(*matrix)]
    sum_diag1 = sum(matrix[i][i] for i in range(len(matrix)))
    sum_diag2 = sum(matrix[i][-i - 1] for i in range(len(matrix)))

    return len(set(sum_row)) == 1 and len(set(sum_col)) == 1 and len(set([sum_diag1, sum_diag2])) == 1


print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
"""
Here, we first calculate the sum of each row, column and both diagonals of the matrix. If all these sums are the same, the matrix is a magic square.

The function returns True if all sums are the same, and False otherwise. 

We use the Python built-in functions set() and len() to check if all sums are the same. If len(set(sums)) == 1, it means all sums are the same, so the matrix is a magic square.
"""

#Q2:
"""
Write a function that takes in an array of integers and returns the sum of all integers in the array, but if the sum exceeds 100, return 0.

assert sum_limit([10, 20, 30, 40, 50]) == 150
assert sum_limit([10, 20, 30, 40, 50, 60, 70]) == 0
"""

A2:
def sum_