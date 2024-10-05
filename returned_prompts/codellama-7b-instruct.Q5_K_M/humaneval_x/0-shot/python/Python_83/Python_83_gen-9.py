
def starts_one_ends(n):
    if n == 1:
        return 10
    else:
        return 9 * (10 ** (n - 2)) + 10
