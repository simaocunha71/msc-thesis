
def check(n):
    if n % 2 == 1:
        return False
    else:
        return n == 2 * (n // 10) - 1


