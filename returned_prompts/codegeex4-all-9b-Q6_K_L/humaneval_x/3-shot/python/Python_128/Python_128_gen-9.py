    if not arr:
        return None

    sign_product = 1
    sum_of_magnitudes = 0

    for num in arr:
        sign_product *= (1 if num >= 0 else -1)
        sum_of_magnitudes += abs(num)

    return sign_product * sum_of_magnitudes

