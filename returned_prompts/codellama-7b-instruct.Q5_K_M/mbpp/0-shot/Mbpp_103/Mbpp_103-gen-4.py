"""
def eulerian_num(n, m):
    if n == 1:
        return 1
    if m == 1:
        return 1
    return (m - 1) * eulerian_num(n - 1, m) + (n - 1) * eulerian_num(n, m - 1)
"""
