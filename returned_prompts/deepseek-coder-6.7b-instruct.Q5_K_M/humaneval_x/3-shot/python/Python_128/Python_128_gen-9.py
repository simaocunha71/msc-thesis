    if not arr:
        return None

    sign_prod = 1
    sum_magnitudes = 0

    for elem in arr:
        sign_prod *= 1 if elem > 0 else -1
        sum_magnitudes += abs(elem)

    return sign_prod * sum_magnitudes


