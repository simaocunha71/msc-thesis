def eulerian_num(n, m):
    if n == 0:
        return 1
    elif m == 0:
        return 0
    else:
        return eulerian_num(n-1, m-1) + m * eulerian_num(n-1, m)