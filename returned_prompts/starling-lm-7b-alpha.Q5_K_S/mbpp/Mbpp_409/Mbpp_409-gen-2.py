def min_product_tuple(tuples):
    min_product = float('inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = tuples[i][0]*tuples[i][1]*tuples[j][0]*tuples[j][1]
            min_product = min(min_product, product)
    return min_product


# tests
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
assert min_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]) == 8
assert min_product_tuple([(3, 4), (5, 6), (7, 8), (9, 10)]) == 18

# Python3 version
def min_product_tuple(tuples):
    min_product = float('inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = tuples[i][0]*tuples[i][1]*tuples[j][0]*tuples[j][1]
            min_product = min(min_product, product)
    return min_product


# tests
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
assert min_product_tuple([(1, 2), (3, 4), (5, 6), (7, 8)]) == 8
assert min_product_tuple([(3, 4), (5, 6), (7, 8), (9, 10)]) == 18

# Python3 version
def min_product_tuple(tuples):
    min_product = float('inf')
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            product = tuples[i][0]*tuples[i][1]*tuples