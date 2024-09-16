def unique_product(my_list):
    # get unique elements in list
    unique_elements = set(my_list)
    # calculate product of unique elements
    product = 1
    for element in unique_elements:
        product *= element
    return product
