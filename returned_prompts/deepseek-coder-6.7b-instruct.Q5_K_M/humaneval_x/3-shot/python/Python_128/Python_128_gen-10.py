    if not arr:
        return None
    prod_sign = 1 if arr[0] >= 0 else -1
    sum_magnitude = abs(arr[0])
    for num in arr[1:]:
        if num > 0:
            prod_sign *= 1
            sum_magnitude += abs(num)
        elif num < 0:
            prod_sign *= -1
            sum_magnitude += abs(num)
        else:
            return 0
    return prod_sign * sum_magnitude


