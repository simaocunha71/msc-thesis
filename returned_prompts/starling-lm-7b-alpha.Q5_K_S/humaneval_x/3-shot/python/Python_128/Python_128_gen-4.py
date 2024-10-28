    if len(arr) == 0:
        return None

    product = 1
    for elem in arr:
        if elem == 0:
            product *= 0
        elif elem > 0:
            product *= 1
        else:
            product *= -1

    return abs(product) * sum(arr)


