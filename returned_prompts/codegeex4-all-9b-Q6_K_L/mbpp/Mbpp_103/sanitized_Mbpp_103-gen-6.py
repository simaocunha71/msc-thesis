def eulerian_num(n, m):
    if n < 0 or m < 0 or m > n:
        return 0
    if n == 0 and m == 0:
        return 1
    if m == 0:
        return 0
    if m == n:
        return 1
    return eulerian_num(n-1, m-1) + m * eulerian_num(n-1, m)