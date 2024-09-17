def min_product_tuple(tuples_list):
    min_product = float('inf')
    for tup1 in tuples_list:
        for tup2 in tuples_list:
            if tup1 != tup2:
                product = tup1[0] * tup2[1]
                if product < min_product:
                    min_product = product
    return min_product