def is_woodall(n):
    s = str(n)
    if len(s) != 3:
        return False
    if int(s[0]) * 100 + int(s[1]) * 10 + int(s[2]) * 1 == n:
        return True
    else:
        return False