def eulerian_num(n, m):
    """
    :param n: int
    :param m: int
    :return: int
    """
    if m > n:
        return 0
    if m == 0 or m == n:
        return 1
    return eulerian_num(n - 1, m) + eulerian_num(n - 1, m - 1)

