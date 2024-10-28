def is_Diff(n):
    while n > 0:
        n, digit = divmod(n, 10)
        if digit > 4:
            return True
    return False