def eulerian_num(n, m):
    if n == 0:
        return 1
    elif m == 0:
        return 0
    else:
        return (n - m) * eulerian_num(n - 1, m) + (m + 1) * eulerian_num(n, m - 1)