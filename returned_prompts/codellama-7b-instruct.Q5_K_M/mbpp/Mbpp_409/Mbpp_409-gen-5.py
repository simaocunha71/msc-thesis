def min_product_tuple(tup_list):
    return min(map(lambda x: x[0]*x[1], tup_list))

# TESTS

def test_min_product_tuple():
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])==8
    assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9), (3, 10)])==8

test_min_product_tuple()

