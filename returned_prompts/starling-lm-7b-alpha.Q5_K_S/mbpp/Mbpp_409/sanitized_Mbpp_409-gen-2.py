def min_product_tuple(tuples):
    min_product = float('inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = tuples[i][0]*tuples[i][1]*tuples[j][0]*tuples[j][1]
            min_product = min(min_product, product)
    return min_product