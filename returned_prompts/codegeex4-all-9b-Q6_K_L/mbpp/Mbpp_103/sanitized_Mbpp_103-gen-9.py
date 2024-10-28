def eulerian_num(n, m):
    """
    Calculate the Eulerian number a(n, m)
    """
    if m > n or m < 0:
        return 0
    elif m == 0 or m == n:
        return 1
    else:
        return (n - 1) * eulerian_num(n - 1, m - 1) + eulerian_num(n - 1, m)