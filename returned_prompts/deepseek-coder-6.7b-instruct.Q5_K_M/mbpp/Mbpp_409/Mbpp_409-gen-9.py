def min_product_tuple(lst):
    return min(a*b for a, b in lst)

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # 8


