def eulerian_num(n, m):
    if n > m:
        return 0
    if n == m:
        return 1
    if n == 1:
        return m
    if m == 1:
        return n
    return (m - 1) * (n - 1) * eulerian_num(n, m - 1) + (m - 1) * eulerian_num(n - 1, m - 1)
