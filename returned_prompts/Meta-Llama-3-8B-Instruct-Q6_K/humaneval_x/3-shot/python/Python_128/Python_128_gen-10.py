    if not arr:
        return None
    signs_product = 1
    for num in arr:
        signs_product *= 1 if num > 0 else -1 if num < 0 else 0
    return sum(abs(num) for num in arr) * signs_product


