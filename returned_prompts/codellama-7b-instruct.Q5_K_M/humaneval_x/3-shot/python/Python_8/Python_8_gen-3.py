    result_sum = 0
    result_product = 1

    for number in numbers:
        result_sum += number
        result_product *= number

    return result_sum, result_product
