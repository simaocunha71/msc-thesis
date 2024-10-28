def is_num_decagonal(n):
    """
    Find the nth decagonal number.
    :param n: int
    :return: int
    """
    return n * (9 * n - 7) // 2