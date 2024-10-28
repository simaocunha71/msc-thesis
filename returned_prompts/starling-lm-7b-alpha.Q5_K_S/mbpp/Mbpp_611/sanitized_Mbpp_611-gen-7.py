def max_of_nth(matrix, n):
    return max([i[n-1] for i in matrix])