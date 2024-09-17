
def max_of_nth(matrix, n):
    return [row[n] for row in matrix].index(max(row for row in matrix))


