def magic_square_test(matrix):
    """
    Function to determine if the given matrix is a magic square.

    Args:
    matrix (list of list of int): The matrix to be checked.

    Returns:
    bool: True if the matrix is a magic square, False otherwise.
    """
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False

    # Check if all rows and columns have the same sum
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(col) for col in zip(*matrix)]
    diag_sum = sum(matrix[i][i] for i in range(len(matrix)))
    anti_diag_sum = sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))

    if len(set(row_sums)) > 1 or len(set(col_sums)) > 1 or diag_sum != row_sums[0] or anti_diag_sum != row_sums[0]:
        return False

    return True