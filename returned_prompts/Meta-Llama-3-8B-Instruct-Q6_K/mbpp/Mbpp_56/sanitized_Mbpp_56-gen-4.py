def check(n):
    reverse_n = int(str(n)[::-1])
    if 2*reverse_n == n+1:
        return True
    else:
        return False