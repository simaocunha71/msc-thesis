    if not numbers:
        return 0, 1

    total_sum = 0
    total_product = 1

    for n in numbers:
        total_sum += n
        total_product *= n

    return total_sum, total_product

