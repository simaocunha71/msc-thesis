def unique_product(my_list):
    # get a list of unique elements
    unique_list = list(set(my_list))
    # initialize the product
    product = 1
    # loop through the list and multiply
    for num in unique_list:
        product *= num
    return product