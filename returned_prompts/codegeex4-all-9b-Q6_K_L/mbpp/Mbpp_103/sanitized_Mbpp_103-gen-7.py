def eulerian_num(n, m):
    """
    Return the Eulerian number a(n, m).
    """
    if m > n:
        return 0
    elif m == 0 or n == m:
        return 1
    else:
        return (n - 1) * eulerian_num(n - 1, m - 1) + eulerian_num(n - 1, m)