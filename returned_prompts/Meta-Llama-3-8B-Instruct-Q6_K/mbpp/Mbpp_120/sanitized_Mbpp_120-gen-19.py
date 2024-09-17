def max_product_tuple(tuples):
    max_product = 0
    for tuple in tuples:
        for i in range(len(tuple)):
            for j in range(len(tuple)):
                if i != j:
                    product = abs(tuple[i] * tuple[j])
                    if product > max_product:
                        max_product = product
    return max_product