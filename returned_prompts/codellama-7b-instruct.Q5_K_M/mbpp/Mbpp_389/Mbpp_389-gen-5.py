def find_lucas(n):
    if n == 2:
        return 1
    if n == 1:
        return 2
    if n == 0:
        return 2
    if n < 0:
        return 0
    return find_lucas(n-1) + find_lucas(n-2)
