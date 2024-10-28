    if not arr:
        return None

    product_of_signs = 1
    for num in arr:
        if num > 0:
            product_of_signs *= 1
        elif num < 0:
            product_of_signs *= -1
        else:
            product_of_signs *= 0

    return sum(arr) * product_of_signs

