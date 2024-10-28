def check(n):
    if int(str(n)[::-1]) == 2*n - 1:
        return True
    return False