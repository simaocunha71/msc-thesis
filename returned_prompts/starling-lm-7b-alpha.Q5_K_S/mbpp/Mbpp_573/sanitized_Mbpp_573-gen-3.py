def unique_product(lst):
    """
    Function to calculate the product of the unique numbers in a given list
    """
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product