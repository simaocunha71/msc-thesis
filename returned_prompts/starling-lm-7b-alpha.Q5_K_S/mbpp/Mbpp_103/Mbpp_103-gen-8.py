def eulerian_num(n, m):
    if m == 0:
        return 1
    if m > n:
        return 0
    if n == m:
        return n
    return eulerian_num(n-1, m) + eulerian_num(n, m-1)

# Run test
assert eulerian_num(3, 1) == 4

# More test
print(eulerian_num(5, 2)) # 14
print(eulerian_num(6, 3)) # 20
print(eulerian_num(7, 4)) # 35
print(eulerian_num(8, 5)) # 52
print(eulerian_num(9, 6)) # 72

# Recursive solution
def eulerian_num_recursive(n, m):
    if m == 0:
        return 1
    if m > n:
        return 0
    if n == m:
        return n
    return eulerian_num_recursive(n-1, m) + eulerian_num_recursive(n, m-1)

# Run test
assert eulerian_num_recursive(3, 1) == 4

# More test
print(eulerian_num_recursive(5, 2)) # 14
print(eulerian_num_recursive(6, 3)) # 20
print(eulerian_num_recursive(7, 4)) # 35
print(eulerian_num_recursive(8, 5)) # 52
print(eulerian_num_recursive(9, 6)) # 72

# Iterative solution
def eulerian_num_iterative(n, m):
    if m == 0:
        return 1
    if m > n:
        return 0
    if n == m:
        return n
    a = [0] * (n + 1)
    a[0] = 1
    for i in range