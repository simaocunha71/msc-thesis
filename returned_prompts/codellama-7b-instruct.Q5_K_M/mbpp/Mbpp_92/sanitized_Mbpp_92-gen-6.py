def is_undulating(num):
    s = list(map(int, str(num)))
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True