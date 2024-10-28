def is_undulating(n):
    s = str(n)
    l = len(s)
    if l < 3:
        return False
    d = int(s[1]) - int(s[0])
    for i in range(2, l):
        if int(s[i]) - int(s[i-1]) != d:
            return False
    return True