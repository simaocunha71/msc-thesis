    for i, v1 in enumerate(l):
        for v2 in l[i + 1:]:
            if v1 + v2 == 0:
                return True

    return False


