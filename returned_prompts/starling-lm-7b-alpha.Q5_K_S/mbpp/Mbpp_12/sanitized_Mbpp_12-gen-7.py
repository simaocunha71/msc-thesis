def sort_matrix(matrix):
    matrix_sums = []
    for i in matrix:
        matrix_sums.append(sum(i))
    sorted_sums = sorted(matrix_sums)
    sorted_matrix = []
    for i in sorted_sums:
        sorted_matrix.append(list(filter(lambda x: sum(x) == i, matrix)))
    return sorted_matrix