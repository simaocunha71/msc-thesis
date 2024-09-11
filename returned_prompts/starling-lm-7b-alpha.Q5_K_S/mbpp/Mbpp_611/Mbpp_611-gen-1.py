def max_of_nth(matrix, n):
    """
    Given a matrix represented as a list of lists, return the max of the n'th column.

    Args:
        matrix (list): A list of lists. Each sublist represents a row of the matrix.
        n (int): The index of the column to get the max of.

    Returns:
        int: The max value of the n'th column.
    """
    return max([row[n] for row in matrix])

# assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], 1) == 6

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], 0) == 3

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], 2) == 6

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], 1000) == None

# assert max_of_nth([], 0) == None

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], -1) == None

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], 3) == 6

# assert max_of_nth([[1, 2, 3], [4, 5, 6]], 0) == 3






























"""
Write a function which given a matrix represented as a list of lists returns the max of the n'th column.

Args:
    matrix (list): A list of lists. Each sublist represents a row of the matrix.
    n (int):