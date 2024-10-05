    if all(i < j for i, j in zip(l, l[1:])):
        return True
    elif all(i > j for i, j in zip(l, l[1:])):
        return True
    else:
        return False

