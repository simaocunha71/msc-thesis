def unique_product(my_list):
    # First get the unique elements of the list
    my_list = list(set(my_list))
    # Then multiply them together
    product = 1
    for i in my_list:
        product *= i
    return product