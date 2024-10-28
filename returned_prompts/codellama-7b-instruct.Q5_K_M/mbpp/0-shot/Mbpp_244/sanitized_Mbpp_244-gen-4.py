def next_Perfect_Square(n):
    """
    :param n: the given number
    :return: the next perfect square greater than n
    """
    while n ** 0.5 % 1 != 0:
        n += 1
    return n