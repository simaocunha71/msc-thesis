def next_Perfect_Square(n):
    root = math.sqrt(n)
    if root == int(root):
        return (root + 1) ** 2
    else:
        return (int(root) + 1) ** 2

