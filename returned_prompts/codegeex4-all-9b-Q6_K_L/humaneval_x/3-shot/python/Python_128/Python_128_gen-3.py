    if not arr:
        return None

    sign_product = 1
    magnitude_sum = 0

    for num in arr:
        sign = 1 if num > 0 else -1 if num < 0 else 0
        magnitude_sum += abs(num)
        sign_product *= sign

    return sign_product * magnitude_sum

