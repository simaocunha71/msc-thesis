def centered_hexagonal_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 7
    else:
        return centered_hexagonal_number(n - 1) + 3 * (2 * n - 1)