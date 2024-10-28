def max_product_tuple(lst):
    max_product = float('-inf')
    for num1, num2 in lst:
        product = abs(num1 * num2)
        if product > max_product:
            max_product = product
    return max_product