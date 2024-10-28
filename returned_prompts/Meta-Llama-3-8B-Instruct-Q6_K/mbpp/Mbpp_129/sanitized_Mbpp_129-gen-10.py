def magic_square_test(matrix):
    total = sum(matrix[0])
    for i in range(len(matrix)):
        if sum(matrix[i]) != total:
            return False
    for j in range(len(matrix[0])):
        if sum([row[j] for row in matrix]) != total:
            return False
    return True