    if not arr:
        return None

    sign_product = 1
    magnitude_sum = 0

    for n in arr:
        if n < 0:
            sign_product *= -1
        magnitude_sum += abs(n)

    return sign_product * magnitude_sum


