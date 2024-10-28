    if not arr:
        return None

    sign_prod = 1
    for num in arr:
        if num < 0:
            sign_prod *= -1
        elif num == 0:
            sign_prod = 0
            break

    return sign_prod * sum(abs(num) for num in arr)

