def max_of_nth(matrix, n):
    return max(row[n] for row in matrix) if n < len(matrix[0]) else None