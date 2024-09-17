
def check(n):
    if n % 2 == 1 and (n - 1) % 2 == 0 and (n // 2 + 1) == (n % 10) * 10 ** (len(str(n)) - 1) + (n // 10) % 10:
        return True
    else:
        return False


