    if len(l) < 2:
        return True
    diff = l[1] - l[0]
    for i in range(1, len(l) - 1):
        if diff * (l[i + 1] - l[i]) < 0:
            return False
    return True


