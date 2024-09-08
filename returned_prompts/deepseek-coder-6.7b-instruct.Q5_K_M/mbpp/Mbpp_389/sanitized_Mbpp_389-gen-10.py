def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    lucas_0 = 2
    lucas_1 = 1
    for _ in range(2, n + 1):
        lucas_0, lucas_1 = lucas_1, lucas_0 + lucas_1
    return lucas_1