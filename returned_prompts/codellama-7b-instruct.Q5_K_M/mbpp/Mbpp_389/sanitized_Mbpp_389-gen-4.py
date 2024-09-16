def find_lucas(n):
    if n < 2:
        return 2
    else:
        return find_lucas(n-1) + find_lucas(n-2)