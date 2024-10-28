def find_lucas(n):
    if n == 0 or n == 1:
        return n
    else:
        return find_lucas(n - 1) + find_lucas(n - 2)