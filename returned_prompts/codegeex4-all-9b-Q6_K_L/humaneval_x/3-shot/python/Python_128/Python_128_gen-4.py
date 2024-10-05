    if not arr:
        return None

    total = 0
    sign = 1

    for num in arr:
        if num < 0:
            sign *= -1
        elif num == 0:
            sign = 0

        total += abs(num)

    return total * sign

