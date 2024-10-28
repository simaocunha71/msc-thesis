def sort_matrix(matrix):
    result = []
    for i in range(len(matrix)):
        result.append((matrix[i], sum(matrix[i])))
    result.sort(key=lambda x: x[1])
    return result
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]