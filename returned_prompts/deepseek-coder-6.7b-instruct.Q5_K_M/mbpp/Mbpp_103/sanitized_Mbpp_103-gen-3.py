def eulerian_num(n, m):
    if m == 0:
        return 1
    elif n < m:
        return 0
    else:
        return eulerian_num(n - 1, m) + eulerian_num(n, m - 1)