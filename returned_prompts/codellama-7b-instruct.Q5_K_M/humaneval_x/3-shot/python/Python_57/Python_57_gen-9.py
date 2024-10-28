    if len(l) < 2:
        return True

    if l[0] < l[1]:
        return all(i >= j for i, j in zip(l, l[1:]))
    elif l[0] > l[1]:
        return all(i <= j for i, j in zip(l, l[1:]))
    else:
        return False


