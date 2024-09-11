def is_nonagonal(n):
    return int(((9*n**2 - 9*n) // 2) + 1)  # formula for nth nonagonal number