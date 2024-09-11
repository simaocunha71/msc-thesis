def check(n):
    reverse = int(str(n)[::-1])
    if 2*reverse - 1 == n:
        return True
    else:
        return False