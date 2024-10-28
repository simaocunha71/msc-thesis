def magic_square_test(matrix):
    n = len(matrix)
    total = sum(matrix[0])
    for row in matrix:
        if sum(row) != total:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != total:
            return False
    return True