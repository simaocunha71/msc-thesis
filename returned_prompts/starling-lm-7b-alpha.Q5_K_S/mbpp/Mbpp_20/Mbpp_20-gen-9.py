
def is_woodall(n):
    s = str(n)
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True
    if int(s[0]) > int(s[1]):
        return False
    for i in range(1, len(s)-1):
        if int(s[i]) < int(s[i+1]):
            return False
    if int(s[len(s)-2]) > int(s[len(s)-1]):
        return False
    else:
        return True


