def magic_square(matrix):
    # Get the sum of each row and each column
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]

    # Get the total sum of the matrix
    total_sum = sum(row_sums)

    # Check if each row, column, and sum of rows and columns are the same
    if len(set(row_sums)) == 1 and len(set(col_sums)) == 1 and len(set(row_sums+col_sums)) == 1 and total_sum % len(matrix) == 0:
        return True
    else:
        return False

# Test the function
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
