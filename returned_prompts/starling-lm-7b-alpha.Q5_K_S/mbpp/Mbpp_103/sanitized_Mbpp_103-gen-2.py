def eulerian_num(n, m):
    if n < m:
        return 0
    if n == m:
        return 1
    if m == 1:
        return n + 1
    if m == 0:
        return 1
    if n == 0:
        return 0
    #if m < 0:
    #    return eulerian_num(n, -m)
    #if m > 0:
    #    return eulerian_num(n - 1, m - 1)
    #if m == 0:
    #    return eulerian_num(n - 1, 0)
    return eulerian_num(n - 1, m) + eulerian_num(n - 1, m - 1)