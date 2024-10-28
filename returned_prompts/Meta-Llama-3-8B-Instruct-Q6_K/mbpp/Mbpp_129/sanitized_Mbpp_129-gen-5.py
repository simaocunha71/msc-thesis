def magic_square_test(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total = sum(matrix[0])
    for i in range(rows):
        if sum(matrix[i]) != total:
            return False
    for i in range(cols):
        if sum([matrix[j][i] for j in range(rows)]) != total:
            return False
    if sum([matrix[i][i] for i in range(rows)]) != total:
        return False
    if sum([matrix[i][rows-i-1] for i in range(rows)]) != total:
        return False
    return True