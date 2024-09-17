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