def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)  # assuming 0-based indexing