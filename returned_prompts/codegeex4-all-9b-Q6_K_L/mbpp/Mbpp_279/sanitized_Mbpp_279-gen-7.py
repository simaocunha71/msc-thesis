def is_num_decagonal(n):
    """
    A decagonal number is a figurate number that extends the concept of triangular and square numbers to the decagon (a ten-sided polygon).
    The nth decagonal number is given by the formula D(n) = n(4n - 3)/2.
    
    :param n: The nth term to find
    :return: The nth decagonal number
    """
    return n * (4 * n - 3) // 2