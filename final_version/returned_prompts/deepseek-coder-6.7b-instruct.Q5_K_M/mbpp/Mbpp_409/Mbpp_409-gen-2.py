
def min_product_tuple(lst):
    min_product = float('inf')
    for tup in lst:
        product = tup[0] * tup[1]
        if product < min_product:
            min_product = product
    return min_product

print(min_product_tuple([(2, 7),  (2, 6),  (1, 8),  (4, 9)]))  # Output: 8


