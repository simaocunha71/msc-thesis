def is_undulating(n):
    s = str(n)
    if len(s) < 3:
        return False
    diff = abs(int(s[0]) - int(s[1]))
    if diff != 2:
        return False
    for i in range(1, len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return False
    return True