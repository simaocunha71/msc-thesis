def is_product_even(lst):
    if not lst:
        return True  # or raise ValueError("List is empty")
    product = 1
    for num in lst:
        product *= num
    return product % 2 == 0