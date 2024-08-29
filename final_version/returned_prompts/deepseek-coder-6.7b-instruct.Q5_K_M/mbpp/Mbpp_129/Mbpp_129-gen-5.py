"""
A magic square is a grid of numbers that satisfies the following conditions:
1. The numbers in each row, column, and diagonal add up to the same number.
2. The numbers are positive integers.

Here is a Python function that checks if a matrix is a magic square:
"""

def magic_square_test(matrix):
    # get the size of the square
    size = len(matrix)

    # calculate the magic constant
    magic_constant = size * (size * size + 1) // 2

    # calculate the row sums
    row_sums = [sum(row) for row in matrix]
    if any(sum != magic_constant for sum in row_sums):
        return False

    # calculate the column sums
    column_sums = [sum(row[i] for row in matrix) for i in range(size)]
    if any(sum != magic_constant for sum in column_sums):
        return False

    # calculate the diagonal sums
    diagonal_sums = [sum(matrix[i][i] for i in range(size)), sum(matrix[i][size - i - 1] for i in range(size))]
    if any(sum != magic_constant for sum in diagonal_sums):
        return False

    return True

# test the function
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
"""
In the above function, we first calculate the magic constant by multiplying the size of the square by size*(size+1)/2.
Then we calculate the sum of each row, column, and diagonal. If any of the sums is not equal to the magic constant, we return False. If all the sums are equal to the magic constant, we return True.
"""

# test the function with a non-magic square
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 