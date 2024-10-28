def eulerian_num(n, m):
    """
    Calculate the Eulerian number a(n, m).
    :param n: int, the first parameter of the Eulerian number
    :param m: int, the second parameter of the Eulerian number
    :return: int, the value of the Eulerian number a(n, m)
    """
    from math import factorial
    return factorial(n + m) // (factorial(n) * factorial(m) * factorial(m + 1))