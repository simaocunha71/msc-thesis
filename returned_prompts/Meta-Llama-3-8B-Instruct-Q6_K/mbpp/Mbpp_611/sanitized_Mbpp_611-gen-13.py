def max_of_nth(matrix, n):
    if not matrix:
        return None
    if n < 0 or n >= len(matrix[0]):
        return None
    return max([row[n] for row in matrix])