def sort_matrix(matrix):
    return [sorted(matrix[i], key=sum) for i in range(len(matrix))]