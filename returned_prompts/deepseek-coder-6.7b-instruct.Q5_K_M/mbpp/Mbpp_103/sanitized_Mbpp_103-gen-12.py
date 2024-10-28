def eulerian_num(n, m):
    if n == 0:
        return 1
    if m == 0:
        return 0
    return (n-1)*eulerian_num(n-1, m) + eulerian_num(n-1, m-1)