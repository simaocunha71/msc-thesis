    # Find the biggest even number in the range
    # [x, y]
    for i in range(x, y + 1):
        if i % 2 == 0:
            return i

    return -1
