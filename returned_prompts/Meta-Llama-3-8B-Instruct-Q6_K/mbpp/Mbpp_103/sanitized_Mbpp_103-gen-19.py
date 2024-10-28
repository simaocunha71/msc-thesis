def eulerian_num(n, m):
    if m > n or m < 0:
        return 0
    if n == 1:
        return 1
    if m == 0:
        return 1
    if m == 1:
        return n - 1
    return (n - 1) * eulerian_num(n - 1, m - 1) + eulerian_num(n - 1, m)