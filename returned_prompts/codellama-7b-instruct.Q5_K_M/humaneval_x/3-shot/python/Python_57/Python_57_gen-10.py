    if len(l) <= 1:
        return True
    elif l[1] < l[0]:
        return all(x >= y for x, y in zip(l[1:], l[:-1]))
    else:
        return all(x <= y for x, y in zip(l[1:], l[:-1]))


