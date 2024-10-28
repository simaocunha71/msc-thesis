    if len(arr) == 0:
        return None

    magnitude_sum = 0
    sign_product = 1

    for num in arr:
        magnitude_sum += abs(num)
        if num < 0:
            sign_product *= -1

    return magnitude_sum * sign_product


