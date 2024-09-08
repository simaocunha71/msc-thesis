def eulerian_num(n, m):
    if m == 0 or m == n:
        return 1
    else:
        return eulerian_num(n - 1, m) + m * eulerian_num(n - 1, m - 1)

# Test cases
print(eulerian_num(3, 1))  # 4
"""
