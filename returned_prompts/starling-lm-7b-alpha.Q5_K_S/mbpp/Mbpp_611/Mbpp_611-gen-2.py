"""
def max_of_nth(matrix, n):
    max_num = 0
    for i in range(len(matrix)):
        if matrix[i][n-1] > max_num:
            max_num = matrix[i][n-1]
    return max_num

def test_max_of_nth():
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 1) == 9
    print("All tests passed")

test_max_of_nth()
"""

def max_of_nth(matrix, n):
    return max(map(lambda x: x[n - 1], matrix))

def test_max_of_nth():
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
    assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 1) == 9
    print("All tests passed")

test_max_of_nth()























"""
def max_of_nth(matrix, n):
    """
    >>> max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)
    19
    >>> max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 1)
    9
    """
    max_num = 0
    for i in range(len(matrix)):
        if matrix[i][n - 1] > max_num