    total = 0
    for elem in lst:
        if isinstance(elem, int) and elem > 0:
            total += elem ** 2
    return total


