    if not numbers:
        return 0, 1

    total = 0
    product = 1

    for num in numbers:
        total += num
        product *= num

    return total, product

