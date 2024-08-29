def eulerian_num(n, m):
    if m == 0:
        return 1
    if n == 0:
        return 0
    return (m + 1) * eulerian_num(n - 1, m) + eulerian_num(n, m - 1)