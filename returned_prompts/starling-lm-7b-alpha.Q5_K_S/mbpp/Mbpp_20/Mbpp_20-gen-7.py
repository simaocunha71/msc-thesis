
def is_woodall(n):
    i = 0
    while n != 0:
        d = n % 10
        if i == d:
            return True
        i += 1
        n = n // 10
    return False


