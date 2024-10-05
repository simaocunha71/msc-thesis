    if not numbers:
        return 0, 1

    result_sum = sum(numbers)
    result_product = 1
    for num in numbers:
        result_product *= num

    return result_sum, result_product


