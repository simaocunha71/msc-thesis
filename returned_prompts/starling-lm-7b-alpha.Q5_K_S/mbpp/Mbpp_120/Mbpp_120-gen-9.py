"""
def max_product_tuple(list_tuple):
    result = 0
    for i in range(len(list_tuple)):
        for j in range(i+1,len(list_tuple)):
            result = max(result, abs(list_tuple[i][0]*list_tuple[j][0]), abs(list_tuple[i][0]*list_tuple[j][1]), abs(list_tuple[i][1]*list_tuple[j][0]), abs(list_tuple[i][1]*list_tuple[j][1]))
    return result

def test_max_product_tuple():
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
    print("All Tests Passed")
test_max_product_tuple()

"""

def max_product_tuple(list_tuple):
    result = 0
    for i in range(len(list_tuple)):
        for j in range(i+1,len(list_tuple)):
            result = max(result, abs(list_tuple[i][0]*list_tuple[j][0]), abs(list_tuple[i][0]*list_tuple[j][1]), abs(list_tuple[i][1]*list_tuple[j][0]), abs(list_tuple[i][1]*list_tuple[j][1]))
    return result

def test_max_product_tuple():
    assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
    print("All Tests Passed")
test_max_product_tuple()






"""
def max_product_tuple(list_tuple):
    max_product = 0
    for i in range(len(list_tuple)):
        for j in range(i+1, len(list_tuple)):
            max_product = max(max_product, abs(list_tuple[i][0]*list_tuple[j][0]), abs(list_tuple[i][0]*list_tuple[j][1]), abs(list