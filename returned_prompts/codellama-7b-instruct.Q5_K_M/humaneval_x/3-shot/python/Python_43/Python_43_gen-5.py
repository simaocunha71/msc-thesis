    for i, x in enumerate(l):
        for y in l[i + 1:]:
            if x + y == 0:
                return True
    return False


