def max_product_tuple(tuples):
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = abs(tuples[i][0] * tuples[i][1] * tuples[j][0] * tuples[j][1])
            max_product = max(max_product, product)
    return max_product