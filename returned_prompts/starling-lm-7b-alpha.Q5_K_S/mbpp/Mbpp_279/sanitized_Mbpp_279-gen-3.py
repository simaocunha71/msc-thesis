def is_num_decagonal(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 2 == 0:
        return False
    if n % 9 == 0:
        return False
    if n % 11 == 0:
        return False
    if n % 5 == 0:
        return False
    if n % 13 == 0:
        return False
    if n % 17 == 0:
        return False
    return True