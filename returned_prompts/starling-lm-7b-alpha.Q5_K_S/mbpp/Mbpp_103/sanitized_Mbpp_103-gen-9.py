def eulerian_num(n, m):
    """
    >>> eulerian_num(3, 1)
    4
    """
    # Your code here
    if n == 0:
        return 0 if m == 0 else 1
    if m == 0:
        return 0
    return eulerian_num(n-1, m) + eulerian_num(n-1, m-1) + (n-m) * eulerian_num(n-1, m-1)