    if x < 0 or y < 0:
        return -1

    for i in range(x, y + 1):
        if i % 2 == 0:
            return i

    return -1


