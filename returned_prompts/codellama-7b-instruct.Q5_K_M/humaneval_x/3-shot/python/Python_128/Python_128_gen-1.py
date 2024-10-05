    if not arr:
        return None

    product = 1
    sum = 0

    for a in arr:
        if a == 0:
            return 0
        elif a > 0:
            product *= 1
        else:
            product *= -1
        sum += abs(a)

    return sum * product
