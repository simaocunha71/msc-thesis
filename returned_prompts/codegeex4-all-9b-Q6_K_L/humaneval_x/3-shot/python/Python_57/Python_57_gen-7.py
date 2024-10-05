    if len(l) <= 1:
        return True

    increasing = l[0] < l[1]
    for i in range(1, len(l) - 1):
        if (increasing and l[i] < l[i + 1]) or (not increasing and l[i] > l[i + 1]):
            continue
        else:
            return False

    return True

