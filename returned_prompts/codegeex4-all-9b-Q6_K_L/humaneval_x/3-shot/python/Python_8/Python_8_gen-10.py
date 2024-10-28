    if not numbers:
        return 0, 1

    sum_numbers = 0
    product_numbers = 1

    for number in numbers:
        sum_numbers += number
        product_numbers *= number

    return sum_numbers, product_numbers

