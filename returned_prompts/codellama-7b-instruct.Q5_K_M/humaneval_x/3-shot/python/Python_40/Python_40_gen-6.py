    l.sort()
    if l[0] > 0:
        return False
    if l[-1] < 0:
        return False
    for i in range(len(l) - 2):
        if l[i] == 0:
            return True
        if l[i] + l[i + 1] == l[i + 2]:
            return True
    return False


