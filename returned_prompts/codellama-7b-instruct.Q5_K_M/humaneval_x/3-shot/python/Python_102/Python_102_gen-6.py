    x, y = sorted((x, y))

    for i in range(x, y + 1, 2):
        if i >= x and i <= y:
            return i

    return -1


