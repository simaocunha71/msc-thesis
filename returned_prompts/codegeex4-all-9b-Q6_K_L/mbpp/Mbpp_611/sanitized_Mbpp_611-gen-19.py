def max_of_nth(matrix: list, n: int) -> int:
    column = [row[n] for row in matrix]
    return max(column)