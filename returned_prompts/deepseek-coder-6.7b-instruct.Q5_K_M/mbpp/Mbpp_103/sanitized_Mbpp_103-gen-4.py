def eulerian_num(n, m):
    if n == 0:
        return 1
    if m == 0 or m > n:
        return 0
    return eulerian_num(n - 1, m) + m * eulerian_num(n - 1, m - 1)