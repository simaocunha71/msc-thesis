def eulerian_num(n, m):
    if m == 0:
        return 1
    elif n == 0:
        return 0
    else:
        return (m * eulerian_num(n - 1, m) + eulerian_num(n, m - 1))


print(eulerian_num(3, 1))

# Output: 4

# 