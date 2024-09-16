def dif_Square(n):
    """
    :param n:
    :return:
    """
    for i in range(1, int(n ** 0.5) + 1):
        if n - i ** 2 == 0:
            return True
    return False