def hexagonal_num(n):
    if n == 1:
        return 1
    else:
        return hexagonal_num(n-1) + n * 2