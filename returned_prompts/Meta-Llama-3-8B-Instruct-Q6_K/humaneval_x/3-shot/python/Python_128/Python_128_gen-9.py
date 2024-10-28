    if not arr:
        return None

    sign_product = 1
    for num in arr:
        sign_product *= 1 if num > 0 else -1 if num < 0 else 0

    total = sum(abs(num) for num in arr)
    return total * sign_product


