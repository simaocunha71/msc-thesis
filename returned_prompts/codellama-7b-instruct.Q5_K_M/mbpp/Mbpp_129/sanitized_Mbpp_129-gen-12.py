def magic_square_test(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if rows != cols:
        return False
    if sum(matrix[0]) != sum(matrix[1]) or sum(matrix[0]) != sum(matrix[2]) or sum(matrix[0]) != sum(matrix[3]):
        return False
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[(i+1) % rows][(j+1) % cols]:
                return False
    return True