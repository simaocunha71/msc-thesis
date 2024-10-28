def eulerian_num(n, m):
    if n < m:
        return 0
    if n == m:
        return 1
    return eulerian_num(n - 1, m) + eulerian_num(n - 1, m - 1)