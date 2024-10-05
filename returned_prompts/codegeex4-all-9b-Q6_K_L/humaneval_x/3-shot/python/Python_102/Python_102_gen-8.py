    if x > y:
        return -1

    for num in range(x, y + 1):
        if num % 2 == 0:
            return num

    return -1

