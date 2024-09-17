
def centered_hexagonal_number(n):
    if n == 1:
        return 1
    return centered_hexagonal_number(n-1) + 1


