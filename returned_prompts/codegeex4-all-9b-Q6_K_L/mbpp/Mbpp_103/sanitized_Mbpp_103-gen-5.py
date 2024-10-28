def eulerian_num(n, m):
    """
    Finds the Eulerian number a(n, m).
    """
    from math import factorial
    return factorial(n) / (factorial(m) * factorial(n - m))