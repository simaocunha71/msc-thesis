    if y < x or y < 0 or x < 0:
        return -1

    if x % 2 == 0:
        return max(x, y)
    else:
        return max(x + 1, y)

