    if not arr:
        return None

    prod_signs = 1
    sum_magnitudes = 0

    for num in arr:
        if num > 0:
            prod_signs *= 1
        elif num < 0:
            prod_signs *= -1
        sum_magnitudes += abs(num)

    return sum_magnitudes * prod_signs


