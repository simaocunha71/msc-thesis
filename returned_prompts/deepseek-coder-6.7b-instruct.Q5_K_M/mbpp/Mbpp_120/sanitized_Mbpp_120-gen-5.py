def max_product_tuple(lst):
    max_prod = 0
    for tup in lst:
        prod = abs(tup[0]*tup[1])
        if prod > max_prod:
            max_prod = prod
    return max_prod