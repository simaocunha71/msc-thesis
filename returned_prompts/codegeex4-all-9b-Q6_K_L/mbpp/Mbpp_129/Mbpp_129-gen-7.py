def magic_square_test(matrix):
    size = len(matrix)
    if size == 0 or size % 2 == 0:
        return False
    total_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != total_sum:
            return False
    for col in range(size):
        if sum(matrix[row][col] for row in range(size)) != total_sum:
            return False
    if sum(matrix[i][i] for i in range(size)) != total_sum:
        return False
    if sum(matrix[i][size-i-1] for i in range(size)) != total_sum:
        return False
    return True

