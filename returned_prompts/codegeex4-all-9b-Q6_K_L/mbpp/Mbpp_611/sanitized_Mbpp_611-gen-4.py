def max_of_nth(matrix, n):
    max_val = float('-inf')
    for row in matrix:
        if n < len(row):
            max_val = max(max_val, row[n])
    return max_val