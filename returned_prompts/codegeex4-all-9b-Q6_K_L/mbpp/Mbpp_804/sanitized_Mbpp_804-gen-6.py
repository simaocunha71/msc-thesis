def is_product_even(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product % 2 == 0