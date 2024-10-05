    if not arr:
        return None

    product_sign = 1
    sum_magnitude = 0

    for num in arr:
        product_sign *= (1 if num > 0 else -1 if num < 0 else 0)
        sum_magnitude += abs(num)

    return sum_magnitude * product_sign


