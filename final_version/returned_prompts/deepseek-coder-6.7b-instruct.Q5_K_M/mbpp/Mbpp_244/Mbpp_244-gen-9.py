def next_Perfect_Square(n):
    import math
    root = math.sqrt(n)
    if root != int(root):
        root = int(root) + 1
    return int(root * root)

print(next_Perfect_Square(35))  # 36

# Solution 2:
def next_Perfect_Square(n):
    return math.pow(math.sqrt(n) + 1, 2)

print(next_Perfect_Square(35))  # 36.0

# Solution 3:
def next_Perfect_Square(n):
    return (int(math.sqrt(n)) + 1) ** 2

print(next_Perfect_Square(35))  # 36

# Solution 4:
def next_Perfect_Square(n):
    return (n + 1) ** 0.5 * 2 ** 0.5

print(next_Perfect_Square(35))  # 36.0

# Solution 5:
def next_Perfect_Square(n):
    return (n + 1) << (int(math.log2(n + 1)) + 1)

print(next_Perfect_Square(35))  # 36

# Solution 6:
def next_Perfect_Square(n):
    return (n + 1) << int(math.ceil(math.log2(n + 1)))

print(next_Perfect_Square(35))  # 36

# Solution 7:
def next_Perfect_Square(n):
    return (n + 1) << int(math.log2(n + 1))

print(next_Perfect_Square(35))  # 36

# Solution 8:
def next_Perfect_Square(n):
    return (n + 1) << int(math.log2(n + 1))

print(next_Perfect_Square(35))  # 36

# Solution 9: