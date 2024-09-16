def is_woodall(n):
    s = str(n)
    if len(s) != 3:
        return False
    for i in range(3):
        if int(s[i]) != i:
            return False
    return True

