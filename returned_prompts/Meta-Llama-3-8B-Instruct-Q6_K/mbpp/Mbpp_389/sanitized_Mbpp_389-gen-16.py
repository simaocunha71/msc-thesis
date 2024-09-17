def find_lucas(n):
    if n <= 1:
        return n
    L1, L2 = 2, 1
    for _ in range(2, n+1):
        L1, L2 = L2, L1 + L2
    return L2