def min_product_tuple(tuples_list):
    min_product = float('inf')
    for tuple1 in tuples_list:
        for tuple2 in tuples_list:
            if tuple1 != tuple2:
                product = tuple1[0] * tuple2[0]
                if product < min_product:
                    min_product = product
    return min_product