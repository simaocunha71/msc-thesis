    if not arr:
        return None

    sign_product = 1
    magnitude_sum = 0

    for num in arr:
        if num < 0:
            sign_product *= -1
            magnitude_sum += abs(num)
        elif num > 0:
            magnitude_sum += num

    return sign_product * magnitude_sum


