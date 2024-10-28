def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != magic_sum:
            return False
    for j in range(n):
        if sum([matrix[i][j] for i in range(n)]) != magic_sum:
            return False
    if sum([matrix[i][i] for i in range(n)]) != magic_sum:
        return False
    if sum([matrix[i][n-i-1] for i in range(n)]) != magic_sum:
        return False
    return True