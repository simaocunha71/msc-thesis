"""
def magic_square_test(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False

    # all rows, cols, and diagonals should add up to the same number
    target = sum(matrix[0])
    for i in range(1, rows):
        if sum(matrix[i]) != target:
            return False
    for j in range(1, cols):
        if sum(matrix[j]) != target:
            return False
    if sum(matrix[0]) != target:
        return False

    return True
"""