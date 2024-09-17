
def is_woodall(n):
    if n == 0:
        return False
    s = sum(list(map(int, str(n))))
    return is_woodall(s) or n == s


