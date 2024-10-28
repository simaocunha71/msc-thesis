    if not arr:
        return None

    total_sum = 0
    sign_prod = 1

    for num in arr:
        if num < 0:
            sign_prod *= -1
        elif num > 0:
            sign_prod *= 1
        else:
            return 0
        total_sum += abs(num)

    return total_sum * sign_prod


