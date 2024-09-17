def unique_product(nums):
    """
    Calculate the product of the unique numbers in a given list.
    """
    unique_nums = set(nums)
    product = 1
    for num in unique_nums:
        product *= num
    return product