    if len(l) < 2:
        return True

    if l[0] < l[-1]:
        for i in range(1, len(l)):
            if l[i] < l[i - 1]:
                return False
    else:
        for i in range(1, len(l)):
            if l[i] > l[i - 1]:
                return False

    return True


