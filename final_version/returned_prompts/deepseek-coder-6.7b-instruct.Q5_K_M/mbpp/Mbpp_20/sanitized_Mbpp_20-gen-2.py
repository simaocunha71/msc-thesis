def is_woodall(n):
    s = str(n)
    l = len(s)
    for i in range(1, l):
        if int(s[:i]) * int(s[i:]) != n:
            return False
    return True