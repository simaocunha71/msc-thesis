    if not arr:
        return None

    sign_prod = 1
    magnitude_sum = 0

    for num in arr:
        sign_prod *= (1 if num > 0 else -1 if num < 0 else 0)
        magnitude_sum += abs(num)

    return magnitude_sum * sign_prod