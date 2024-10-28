    if not arr:
        return None

    magnitude_sum = 0
    product = 1

    for num in arr:
        if num == 0:
            magnitude_sum += 0
            product *= 0
        elif num > 0:
            magnitude_sum += num
            product *= 1
        else:
            magnitude_sum += abs(num)
            product *= -1

    return magnitude_sum * product
