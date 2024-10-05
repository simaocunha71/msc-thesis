    if not arr:
        return None

    positive_signs = 1
    negative_signs = 1
    zero_signs = 0

    for num in arr:
        if num > 0:
            positive_signs *= 1
        elif num < 0:
            negative_signs *= -1
        else:
            zero_signs *= 0

    return negative_signs * positive_signs * zero_signs


