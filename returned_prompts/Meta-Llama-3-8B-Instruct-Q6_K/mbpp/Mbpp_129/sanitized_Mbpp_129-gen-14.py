def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    for col in range(n):
        if sum([matrix[row][col] for row in range(n)]) != magic_sum:
            return False
    if sum([matrix[i][i] for i in range(n)]) != magic_sum:
        return False
    if sum([matrix[i][n-i-1] for i in range(n)]) != magic_sum:
        return False
    return True