
def eulerian_num(n, m):
    if n == 0:
        return 0
    if m == 0:
        return 0
    if n == 1 or m == 1:
        return 1
    return eulerian_num(n, m - 1) + m * eulerian_num(n - 1, m)


