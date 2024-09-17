
def max_product_tuple(tup):
    max_product = 0
    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            product = tup[i][0] * tup[i][1] * tup[j][0] * tup[j][1]
            if product > max_product:
                max_product = product
    return max_product


