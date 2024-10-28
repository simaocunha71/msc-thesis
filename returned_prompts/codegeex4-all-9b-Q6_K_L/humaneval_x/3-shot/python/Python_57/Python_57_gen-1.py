    if len(l) <= 1:
        return True

    increasing = l[0] < l[1]
    for i in range(1, len(l)-1):
        if (l[i] < l[i-1]) != increasing:
            return False

    return True

