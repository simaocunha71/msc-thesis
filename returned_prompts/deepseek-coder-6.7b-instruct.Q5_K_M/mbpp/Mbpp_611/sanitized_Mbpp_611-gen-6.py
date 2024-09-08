def max_of_nth(matrix, n):
    column = [row[n] for row in matrix]
    return max(column)