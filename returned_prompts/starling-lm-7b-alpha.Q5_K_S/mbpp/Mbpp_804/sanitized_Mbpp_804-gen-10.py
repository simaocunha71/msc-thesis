def is_product_even(numbers):
    """
    Determine if the product of numbers in a list is even.

    >>> is_product_even([1,2,3])
    True
    """
    product = 1
    for num in numbers:
        product *= num
    return product % 2 == 0