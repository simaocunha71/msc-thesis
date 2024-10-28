def centered_hexagonal_number(n):
    if n == 1:
        return 1
    else:
        return centered_hexagonal_number(n - 1) + (2 * (n - 1))