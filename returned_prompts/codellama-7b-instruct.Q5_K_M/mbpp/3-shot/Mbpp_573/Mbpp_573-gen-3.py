
def unique_product(my_list):
    unique_elements = set(my_list)
    product = 1
    for i in unique_elements:
        product *= i
    return product


