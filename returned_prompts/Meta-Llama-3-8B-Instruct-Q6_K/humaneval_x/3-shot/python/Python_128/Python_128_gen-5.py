    if not arr:
        return None
    sign = 1
    magnitude_sum = 0
    for num in arr:
        if num < 0:
            sign *= -1
        magnitude_sum += abs(num)
    return sign * magnitude_sum


