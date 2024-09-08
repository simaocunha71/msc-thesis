def sort_matrix(matrix):
    # Calculate the sum of each row
    row_sums = [sum(row) for row in matrix]
    # Sort the matrix based on the sum of each row
    sorted_matrix = sorted(matrix, key=lambda row: sum(row))
    return sorted_matrix