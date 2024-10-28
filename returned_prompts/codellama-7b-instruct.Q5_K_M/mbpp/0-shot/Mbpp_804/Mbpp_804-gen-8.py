def is_product_even(my_list):
    product = 1
    for i in my_list:
        product *= i
    return product % 2 == 0

