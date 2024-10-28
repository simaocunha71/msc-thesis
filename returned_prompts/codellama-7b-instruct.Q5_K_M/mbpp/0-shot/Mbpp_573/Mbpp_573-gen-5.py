def unique_product(my_list):
    """
    Calculate the product of the unique numbers in a given list
    """
    unique_list = list(set(my_list))
    product = 1
    for i in unique_list:
        product *= i
    return product
