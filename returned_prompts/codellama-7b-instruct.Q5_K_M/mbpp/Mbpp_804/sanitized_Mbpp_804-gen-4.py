def is_product_even(my_list):
    product = 1
    for number in my_list:
        product *= number
    return product % 2 == 0