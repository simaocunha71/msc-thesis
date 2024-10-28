def eulerian_num(n, m):
    if m == 0:
        return 1
    elif n == m:
        return 0
    else:
        return (n - 1) * eulerian_num(n - 1, m - 1) + eulerian_num(n - 1, m)

