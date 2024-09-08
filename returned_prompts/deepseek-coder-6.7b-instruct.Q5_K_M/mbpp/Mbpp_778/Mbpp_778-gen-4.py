def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    total = 0
    sign = 1

    for fc in range(len(matrix[0])):
        sub_matrix = [row[:fc] + row[fc+1:] for row in matrix[1:]]
        sign = -sign
        total += sign * matrix[0][fc] * determinant(sub_matrix)

    return total