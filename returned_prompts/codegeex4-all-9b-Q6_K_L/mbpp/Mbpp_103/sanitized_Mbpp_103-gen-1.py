def eulerian_num(n, m):
    if m == 0:
        return 1
    else:
        return eulerian_num(n, m-1) + n * eulerian_num(n-1, m-1)