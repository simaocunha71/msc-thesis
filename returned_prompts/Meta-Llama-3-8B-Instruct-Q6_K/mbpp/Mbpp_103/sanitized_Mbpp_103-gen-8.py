def eulerian_num(n, m):
    if m == 0:
        return 1
    else:
        return (n + m - 1) * eulerian_num(n - 1, m - 1) // m