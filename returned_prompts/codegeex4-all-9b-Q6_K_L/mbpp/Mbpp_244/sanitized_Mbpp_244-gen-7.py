def next_Perfect_Square(n):
    if n < 0:
        return -1
    root = int(n**0.5)
    if root**2 == n:
        return (root + 1)**2
    else:
        return root**2 + 2*root + 1