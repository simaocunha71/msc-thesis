def check(n):
    if n < 0:
        return False
    rev = int(str(n)[::-1])
    return (n == rev * 2 - 1)