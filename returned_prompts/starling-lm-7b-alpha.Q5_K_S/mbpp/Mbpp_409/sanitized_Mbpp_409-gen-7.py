def min_product_tuple(tup):
    min_prod = tup[0][0] * tup[0][1]
    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            if tup[i][0] * tup[i][1] * tup[j][0] * tup[j][1] < min_prod:
                min_prod = tup[i][0] * tup[i][1] * tup[j][0] * tup[j][1]
    return min_prod