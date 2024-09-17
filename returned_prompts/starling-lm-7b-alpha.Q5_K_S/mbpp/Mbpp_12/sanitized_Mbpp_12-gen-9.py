def sort_matrix(matrix):
    # Sort the matrix by the sum of its rows
    sorted_matrix = sorted(matrix, key=lambda x: sum(x))
    return sorted_matrix
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]