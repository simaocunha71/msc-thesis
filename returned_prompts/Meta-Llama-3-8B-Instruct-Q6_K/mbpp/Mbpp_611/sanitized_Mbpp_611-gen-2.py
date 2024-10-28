def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])  # or return max([x for row in matrix for x in [row[n]]]) if you want to use list comprehension