def magic_square_test(matrix):
    n = len(matrix)
    total = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != total:
            return False
    for j in range(n):
        total = sum([matrix[i][j] for i in range(n)])
        if total != total:
            return False
    total = sum([matrix[i][i] for i in range(n)])
    if total != total:
        return False
    total = sum([matrix[i][n-i-1] for i in range(n)])
    if total != total:
        return False
    return True