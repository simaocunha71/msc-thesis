def is_product_even(my_list):
    result = 1
    for element in my_list:
        result *= element
    return result % 2 == 0

