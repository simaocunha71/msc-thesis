def is_woodall(n):
    s = str(n)
    if len(s) != 3:
        return False
    if s[1] != '0':
        return False
    return int(s[0]) % 2 == 0 and int(s[2]) % 2 == 0
