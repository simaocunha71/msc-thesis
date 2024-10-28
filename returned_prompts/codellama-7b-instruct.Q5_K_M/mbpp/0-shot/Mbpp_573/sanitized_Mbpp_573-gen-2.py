def unique_product(my_list):
    my_list = list(set(my_list))
    product = 1
    for i in my_list:
        product *= i
    return product