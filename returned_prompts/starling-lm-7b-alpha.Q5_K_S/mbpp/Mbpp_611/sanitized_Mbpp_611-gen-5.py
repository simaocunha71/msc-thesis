def max_of_nth(matrix, n):
    assert type(matrix) == list and type(n) == int
    if n >= len(matrix[0]):
        return None
    res = []
    for i in matrix:
        res.append(i[n])
    return max(res)