def min_product_tuple(lst):
    return min([i[0]*i[1] for i in lst])

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

