"""
def max_subarray_product(my_list):
    min_product = 1
    max_product = 1
    for x in my_list:
        if x < 0:
            min_product, max_product = max_product, min_product
        min_product = min(min_product, x)
        max_product = max(max_product, x)
    return max(min_product * max_product, max_product * min_product)
"""

