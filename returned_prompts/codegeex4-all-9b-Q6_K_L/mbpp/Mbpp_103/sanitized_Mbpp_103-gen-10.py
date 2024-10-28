def eulerian_num(n, m):
    if n < 0 or m < 0:
        return 0
    if n == 0 or m == 0:
        return 1
    return eulerian_num(n - 1, m) + m * eulerian_num(n - 1, m - 1)