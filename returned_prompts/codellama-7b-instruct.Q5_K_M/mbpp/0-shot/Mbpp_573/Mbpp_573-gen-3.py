def unique_product(my_list):
    # get unique elements in the list
    unique_elements = set(my_list)
    # calculate the product
    product = 1
    for element in unique_elements:
        product *= element
    return product

