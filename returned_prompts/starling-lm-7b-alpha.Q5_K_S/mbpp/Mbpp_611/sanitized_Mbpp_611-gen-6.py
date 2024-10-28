def max_of_nth(matrix, n):
    if isinstance(matrix, list) and all(isinstance(i, list) for i in matrix):
        if isinstance(n, int) and n >= 0:
            return max([row[n] for row in matrix])
    raise ValueError("Incorrect input format")